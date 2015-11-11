#!/usr/bin/env python3

import sys

from PIL import Image
from dxt import Encoder
from dxtutil import DXT1

if __name__ == "__main__":
    image_file = sys.argv[1]
    print("Converting image {} to dxt1".format(image_file))

    image = Image.open(image_file)
    dxt1_encoded = Encoder(image)

    print("exporting")
    # export the DXT1-encoded image as PNG
    # to make sure your encoder worked properly
    print(' 0x'.join('{:02x}'.format(x) for x in dxt1_encoded.compressed), len(dxt1_encoded.compressed))
    print("image size:", image.size)
    dxt = DXT1(dxt1_encoded.compressed, image.size)
    dxt.export_png(image_file[:-4] + "_dxt1.png")
