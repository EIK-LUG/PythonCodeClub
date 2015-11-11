"""
S3 DXT1 image compression lib

Author: Arti Zirk
"""

import struct

class Encoder():

    def __init__(self, image):
        self.image = image  # image that we will compress
        self.pixels = image.load()  # image data

        self.compressed = bytearray()  # compressed dxt1 image data
        self.blocks = []

        for i, block in enumerate(self.block_generator()):
            print(i, len(block))
            cblock = []  # compressed block
            palette = self.get_palette(block)

            for pixel in block:
                cblock.append(self.map_to_pallete(palette, pixel))

            palette = (self.rgb888to565(palette[0]), self.rgb888to565(palette[1]))
            self.compressed.extend(self.pack_block(cblock, palette))

    def pack_block(self, block, palette):
        pixels = 0
        for i, pixel in enumerate(block):
            pixels = (pixel << 2*i) | pixels
        #print(block)
        #print(len(bin(palette[0])[2:]), len(bin(palette[1])[2:]))
        #print(len(bin(pixels)[2:]))
        return struct.pack("HHI", palette[0], palette[1], pixels)

    def rgb888to565(self, color):
        """Converts a color in rgb888 format to rgb565"""
        r = color[0]
        g = color[1]
        b = color[2]
        return ((r >> 3) << 11) | ((g >> 2) << 5) | b >> 3

    def map_to_pallete(self, palette, pixel):
        diff = []
        for color in palette:
            diff.append(abs(sum(color)-sum(pixel)))

        return diff.index(min(diff))

    def get_palette(self, block):
        """Gives us the two colors of a image block that are used as a pallete"""
        p = [max(block), min(block), 0, 0]
        p[2] = tuple(int(2/3 * p[0][x] + 1/3 * p[1][x]) for x in range(3))
        p[3] = tuple(int(1/3 * p[0][x] + 2/3 * p[1][x]) for x in range(3))
        return p

    def block_generator(self):
        """Generates blocks of 4x4 imagedata from source data"""
        (imagex, imagey) = self.image.size
        for block_start_y in range(0, imagey, 4):
            for block_start_x in range(0, imagex, 4):
                print("blockstart:", block_start_x, block_start_y)
                block = []
                for data_y in range(block_start_y, block_start_y+4):
                    for data_x in range(block_start_x, block_start_x+4):
                        try:
                            block.append(self.pixels[data_x, data_y])
                        except IndexError as err:
                            block.append((0, 0, 0))  # add a black pixel
                yield block

    def save_to_file(self):
        raise NotImplementedError("saving to a file is not yet implemented")
