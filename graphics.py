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
    self.buffer = [[Graphics.OFF for i in range(self.height)] for i in range(self.width)]

  def pyxel_update(self):
    self.buffer[4][10] = Graphics.ON

  def pyxel_draw(self):
    for x in range(self.width):
      for y in range(self.height):
        pyxel.pix(x, y, self.buffer[x][y])

test = Graphics()
