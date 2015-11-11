"""
A DXT->PNG converter for the DXT1 Python Codeclub exercise.

@author Romet
"""
from struct import unpack
from PIL import Image


def decode_rgb565(val):
    """Decode a RGB565 uint16 into a RGB888 tuple."""
    r5 = (val & 0xf800) >> 11
    g6 = (val & 0x7e0) >> 5
    b5 = val & 0x1f
    return (
        int((r5 * 255 + 15) / 31),
        int((g6 * 255 + 31) / 63),
        int((b5 * 255 + 15) / 31)
    )


def expand_palette(palette):
    """Generate 2 additional colours from an existing palette."""
    col1 = palette[0]
    col2 = palette[1]
    col3 = tuple(int(2/3 * col1[x] + 1/3 * col2[x]) for x in range(3))
    if sum(col2) < sum(col1):
        col4 = tuple(int(1/3 * col1[x] + 2/3 * col2[x]) for x in range(3))
    else:
        col4 = (0, 0, 0, 0)
    return [col1, col2, col3, col4]


class DXT(object):

    """A base class to contain and decode DXT-encoded image buffers."""

    def __init__(self, image_data, size_tuple):
        """Initialize and decode a DXT object."""
        (self.img_width, self.img_height) = size_tuple
        self.pixels = []

        for i in range(0, len(image_data), 8):
            palette_buf = image_data[i:i+4]
            indices_buf = image_data[i+4:i+8]

            palette = [decode_rgb565(col) for col in unpack("HH", palette_buf)]
            palette = expand_palette(palette)

            for row_int in indices_buf:
                for bit_idx in range(0, 8, 2):
                    palette_idx = (row_int >> bit_idx) & 3
                    self.pixels.append(palette[palette_idx])

    def get_pil_image(self):
        """An abstract method placeholder for get_pil_image."""
        raise NotImplementedError

    def export_png(self, filename, scale=1):
        """Export the DXT buffer as a PNG image using PIL."""
        img = self.get_pil_image()
        if scale > 1:
            orig_size = img.size
            new_size = (orig_size[0] * scale, orig_size[1] * scale)
            img = img.resize(new_size, Image.NEAREST)
        img.save(filename, "PNG")


class DXT1(DXT):

    """A class to contain, decode and export DXT1-encoded image buffers."""

    def get_pil_image(self):
        """Create a PIL Image from DXT1 chunks."""
        img = Image.new("RGBA", (self.img_width, self.img_height), "black")
        img_pixels = img.load()

        pixel_count = len(self.pixels)
        chunk_count = pixel_count // 16
        chunks_wide = chunk_count // (self.img_height // 4)
        print("chunks_wide", chunks_wide)
        print("chunk_count", chunk_count)

        for chunk_idx in range(chunk_count):
            chunk_x = chunk_idx % chunks_wide
            chunk_y = chunk_idx // chunks_wide
            print("chunk:", chunk_x, chunk_y)

            for col_idx in range(16):
                x = col_idx % 4 + chunk_x * 4
                y = col_idx // 4 + chunk_y * 4
                print(x, y)

                try:
                    img_pixels[x, y] = self.pixels[chunk_idx * 16 + col_idx]
                except:
                    print("out of range")
        return img
