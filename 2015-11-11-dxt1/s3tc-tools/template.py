"""
An awesome solution to the DXT1 Python Codeclub exercise.

@author You
"""
from dxtutil import DXT1
from PIL import Image


def encode_dxt1(image):
    """Encode a PIL Image into DXT1 (stored in bytearray)."""
    pixels = image.load()
    # you can access the colours in the image by indexing:
    # pixels[x, y]
    # => (red, green, blue)
    # for example, pixels[0, 0] returns (r, g, b) for the top-left pixel
    # for more info, see the PIL docs:
    # http://pillow.readthedocs.org/en/3.0.x/reference/Image.html

    image_data = bytearray()
    # this is just sample_small.png in DXT1, replace
    # the following with your encoding code
    image_data.extend([0xE6, 0x81, 0xE9, 0x48, 0xB5, 0xBD, 0x2F, 0x0B])
    image_data.extend([0xE3, 0xC2, 0xE6, 0x81, 0xB5, 0xAD, 0x2F, 0x0B])
    return image_data

if __name__ == '__main__':
    img_name = "sample_small"
    # img_name = "sample"

    # use PIL to read the input PNG file
    sample_image = Image.open(img_name + ".png")

    # create a DXT1-encoded bytearray from the PNG
    dxt1_data = encode_dxt1(sample_image)

    # export the DXT1-encoded image as PNG
    # to make sure your encoder worked properly
    dxt = DXT1(dxt1_data, sample_image.size)
    dxt.export_png(img_name + "_dxt1.png")
