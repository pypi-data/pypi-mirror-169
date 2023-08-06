from .Core import *
import numpy
import matplotlib.cm as cm

class ColorMapping(Filter):

    def __init__(self):
        super().__init__()

        self.addInputPort("Map", "plasma")
        self.addInputPort("NaN", (0,0,0,0))
        self.addInputPort("Range", (0,1))
        self.addInputPort("Channel", "Depth")
        self.addInputPort("Images", [])
        self.addOutputPort("Images", [])

    def update(self):
        super().update()

        images = self.inputs.Images.get()

        results = []

        cmap = cm.get_cmap( self.inputs.Map.get() )
        cmap.set_bad(color=self.inputs.NaN.get() )
        r = self.inputs.Range.get()
        d = r[1]-r[0]
        for image in images:
            result = image.copy()
            channel = result.channel[ self.inputs.Channel.get() ]
            normalized = (channel-r[0])/d
            result.channel["RGBA"] = cmap(normalized, bytes=True)
            results.append(result)

        self.outputs.Images.set(results)

        return 1
