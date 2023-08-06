from .Core import *

import numpy
import h5py
import os
import csv
import hashlib

class ImageWriter(Filter):

    def __init__(self):
        super().__init__()
        self.addInputPort("Path", "")
        self.addInputPort("Images", [])

    def getImageHash(self,image):
        keys = list(image.meta.keys())
        keys.sort()
        text = ""
        for k in keys:
            text = text + str(image.meta[k]) + ';'
        h = int(hashlib.md5(text.encode('utf-8')).hexdigest(), 16)
        return h

    def writeH5(self,path,image):
        file = h5py.File(path, 'w')

        file.create_dataset('origin', data=image.origin)

        fChannel = file.create_group('channel')
        for k in image.channel:
            fChannel.create_dataset(k,data=image.channel[k], compression='gzip', compression_opts=9)

        fMeta = file.create_group('meta')
        for k in image.meta:
            data = image.meta[k]
            if type(data) is numpy.ndarray and data.size>1:
                fMeta.create_dataset(k,data=data, compression='gzip', compression_opts=9)
            else:
                fMeta.create_dataset(k,data=data)

        file.close()

    def update(self):
        super().update()

        images = self.inputs.Images.get()
        path = self.inputs.Path.get()

        if len(images)<1:
            return 1

        # check if path is a cdb
        filename, extension = os.path.splitext(path)
        extension = str.lower(extension[1:])
        if extension == 'cdb':
            # cdb folder

            csvPath = path+'/data.csv'
            csvData = []

            if os.path.exists(csvPath):
                with open(csvPath, 'r+') as csvfile:
                    rows = csv.reader(csvfile, delimiter=',')
                    for row in rows:
                        csvData.append(row)
            else:
                image0 = images[0]
                header = list(image0.meta.keys())
                header.append('FILE')
                csvData.append(header)

            # build meta to idx map
            metaIdxMap = {}
            for (k,v) in enumerate(csvData[0]):
                metaIdxMap[v] = k

            # check if each image already exists in CDB
            for image in images:
                dbRowIdx = -1

                imageHash = self.getImageHash(image)
                fileName = str(imageHash)+'.h5'

                fileColumnIdx = metaIdxMap['FILE']
                for i in range(1,len(csvData)):
                    if csvData[i][fileColumnIdx] == fileName:
                        dbRowIdx = i
                        break
                    # row = csvData[i]
                    # allRowValuesAreEqual = True

                    # for m in image.meta:
                    #     idx = metaIdxMap[m]
                    #     if idx == None:
                    #         raise ValueError('Image has meta entry not recorded in CDB')
                    #     if row[idx] != str(image.meta[m]):
                    #         allRowValuesAreEqual = False
                    #         break

                    # if allRowValuesAreEqual:
                    #     dbRowIdx = i
                    #     break

                if dbRowIdx<0:
                    newRow = [None]*len(csvData[0])
                    newRow[metaIdxMap['FILE']] = fileName
                    for m in image.meta:
                        idx = metaIdxMap[m]
                        if idx == None:
                            raise ValueError('Image has meta information not recorded in CDB')
                        newRow[idx] = str(image.meta[m])
                    csvData.append(newRow)

                    with open(csvPath, 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                        for row in csvData:
                            writer.writerow(row)

                self.writeH5(path+'/'+fileName,image)

        elif extension == '':
            # normal folder
            for i,image in enumerate(images):
                self.writeH5(path+str(i)+'.h5',image)

        return 1
