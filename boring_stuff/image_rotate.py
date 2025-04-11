from PIL import Image

catIm = Image.open('zophie.png')
catIm.rotate(90).save('rotated90.jpg')
catIm.rotate(180).save('rotated180.jpg')
catIm.rotate(270).save('rotated270.jpg')
catIm.rotate(6, expand=True).save('rotated6_expanded.jpg')
catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.jpg')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.jpg')

