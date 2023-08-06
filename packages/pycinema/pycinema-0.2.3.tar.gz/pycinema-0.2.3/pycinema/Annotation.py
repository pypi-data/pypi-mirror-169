from .Core import *
import PIL
import numpy
import sys

class Annotation(Filter):

    def __init__(self):
        super().__init__()

        self.addInputPort("XY", (20,20))
        self.addInputPort("Size", 20)
        self.addInputPort("Spacing", 0)
        self.addInputPort("Color", 'AUTO')
        self.addInputPort("Images", [])
        self.addInputPort("Ignore", ['FILE'])
        self.addOutputPort("Images", [])

    #
    # solution from:
    # https://www.programcreek.com/python/?CodeExample=get+font
    #
    def __get_font(self, size):
        """Attempts to retrieve a reasonably-looking TTF font from the system.

        We don't make much of an effort, but it's what we can reasonably do without
        incorporating additional dependencies for this task.
        """
        if sys.platform == 'win32':
            font_names = ['Arial']
        elif sys.platform in ['linux', 'linux2']:
            font_names = ['DejaVuSans-Bold', 'DroidSans-Bold']
        elif sys.platform == 'darwin':
            font_names = ['Menlo', 'Helvetica']

        font = None
        for font_name in font_names:
            try:
                font = PIL.ImageFont.truetype(font_name, size)
                break
            except IOError:
                continue

        return font

    def update(self):
        super().update()

        images = self.inputs.Images.get()

        results = []
        if len(images)<1:
          self.outputs.Images.set(results)
          return 1

        textColor = self.inputs.Color.get()
        if textColor=='AUTO':
            mean = images[0].channel['RGBA'].mean(axis=(0,1))
            if (mean[0]+mean[1]+mean[2])/3<128:
                textColor = (255,255,255)
            else:
                textColor = (0,0,0)

        font = self.__get_font(self.inputs.Size.get())

        ignoreList = list(map(str.lower, self.inputs.Ignore.get()))

        for image in images:
            rgba = image.channel["RGBA"]
            rgbImage = PIL.Image.fromarray( rgba )
            text = ''
            for t in image.meta:
                if t.lower() in ignoreList:
                    continue
                text = text + ' ' + t+': '+str(image.meta[t]) + '\n'

            I1 = PIL.ImageDraw.Draw(rgbImage)
            I1.multiline_text(
                self.inputs.XY.get(),
                text,
                fill=textColor,
                font=font,
                spacing=self.inputs.Spacing.get()
            )

            outImage = image.copy()
            outImage.channel['RGBA'] = numpy.array(rgbImage)
            results.append( outImage )

        self.outputs.Images.set(results)

        return 1
