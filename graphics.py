import pyxel
# import constants

class Graphics():
    ON = 7
    OFF = 0

    def __init__(self, width=64, height=32, scale=10):
        # buffers
        self.width = width
        self.height = height
        self.reset_buffer()
        # graphics engine
        pyxel.init(self.width, self.height, scale=scale)
        pyxel.run(self.pyxel_update, self.pyxel_draw)

    def reset_buffer(self):
        self.buffer = [[Graphics.OFF for i in range(self.width)] for i in range(self.height)]

    def draw_sprite(self, x, y, sprite_data):
        pos_y = y & self.height
        for data in sprite_data:
            pos_x = x & self.width
            for bit in bin(data)[2:]:
                value = Graphics.ON if bit == '1' else Graphics.OFF
                self.set_pixel(pos_x, pos_y, value)
                pos_x += 1
            pos_y += 1

    def set_pixel(self, x, y, value):
        self.buffer[y % self.height][x % self.width] = value

    def pyxel_update(self):
        self.draw_sprite(2, 2, [5, 30, 100, 75])

    def pyxel_draw(self):
        for y in range(self.height):
            for x in range(self.width):
                pyxel.pix(x, y, self.buffer[y][x])


test = Graphics()
