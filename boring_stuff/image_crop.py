from PIL import Image

catIm = Image.open('zophie.png')
croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save('cropped.jpg')

catCopyIm = catIm.copy()
faceIm = catIm.crop((335, 345, 565, 560))
print(faceIm.size)
catCopyIm.paste(faceIm, (0, 0))
catCopyIm.paste(faceIm, (400, 500))
catCopyIm.save('pasted.jpg')

catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()
for left in range(0, catImWidth, faceImWidth):
    for top in range(0, catImHeight, faceImHeight):
        print(left, top)
        catCopyTwo.paste(faceIm, (left, top))

catCopyTwo.save('tiled.jpg')