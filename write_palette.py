from PIL import Image, ImageDraw

def write_palette(colors):
  width = 50
  height = 100
  total_width = len(colors) * width

  im = Image.new('RGB', (total_width, height), 'white')
  draw = ImageDraw.Draw(im)
  for index, color in enumerate(colors):
    x = index * width
    draw.rectangle([x,0,x+width,height], fill=color.hex)
  im.save('colors.png')

