from PIL import Image, ImageColor

im = Image.new('RGBA', (100, 200))
print(im.getpixel((0, 0)))
for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (210,210,210))


for x in range(100):
    for y in range(50,100):
        im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
print(im.getpixel((0, 0)))
print(im.getpixel((0, 50)))        
im.save('putPixel.png')