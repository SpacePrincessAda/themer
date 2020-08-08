import colorsys

class Color:
  def __init__(self, h, s, v):
    self.h = h
    self.s = s
    self.v = v

  @property
  def hex(self):
    rgb = colorsys.hsv_to_rgb(self.h/360, self.s/100, self.v/100)
    return '#{:02x}{:02x}{:02x}'.format(*[round(v*255) for v in rgb])

