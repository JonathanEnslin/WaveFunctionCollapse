from PIL import Image, ImageDraw

# create a 20x20 pixel black image containing a 10x10 px blue square, and a single red pixel in one corner
im = Image.new('RGB', (4, 4), (0, 0, 0))
draw = ImageDraw.Draw(im)
draw.rectangle([(0, 0), (1, 1)], fill=(0, 0, 255))
im.putpixel((1, 1), (255, 0, 0))

# display the image in png format
im.save('test.png')



