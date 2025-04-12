#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from pathlib import Path
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FIT_SIZE = 50
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size
if logoWidth > LOGO_FIT_SIZE and logoHeight > LOGO_FIT_SIZE:
    if logoWidth > logoHeight:
        logoHeight = int((LOGO_FIT_SIZE / logoWidth) * logoHeight)
        logoWidth = LOGO_FIT_SIZE
    else:
        logoWidth = int((LOGO_FIT_SIZE / logoHeight) * logoWidth)
        logoHeight = LOGO_FIT_SIZE
print(f'Resize logo to {logoWidth}, {logoHeight}')
logoIm = logoIm.resize((logoWidth, logoHeight))

cwd=Path.cwd()

destDir = 'withlogo'
# destDir = os.path.join(cwd, destDir)
os.makedirs(destDir, exist_ok=True)

for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
            or filename == LOGO_FILENAME:
        continue
    im = Image.open(filename)
    width, height = im.size
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        print(f'Resizing {filename} to {width},{height} ...')
        im = im.resize((width, height))
    print(f'Adding logo to {filename}...')
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    sFileOut = os.path.join('withLogo', filename)
    print(f'Saving to {sFileOut}')
    im.save(sFileOut)