import zipfile, os
from pathlib import Path
import sys
import send2trash 

p = Path.cwd()
exampleZip = zipfile.ZipFile(p / 'spam.zip')
print(exampleZip.namelist())

spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo)
print(f'file_size={spamInfo.file_size}')

print(f'compress_size={spamInfo.compress_size}')

print(f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!')

exampleZip.close()

d = Path(p / 'somefolder')
if not d.exists():
    os.mkdir(d)
if not d.is_dir():    
    print(f'{d} is not directory' )
    sys.exit() 
# for fn in os.listdir(d):
    # filename=os.path.join(d / fn)
    # print(f'send2trash({filename})')
    # send2trash.send2trash(filename)

for filename in d.glob('*.txt'):      
    print(f'send2trash({filename})')
    send2trash.send2trash(filename)
    # os.unlink(filename)

exampleZip = zipfile.ZipFile(p / 'spam.zip')
# exampleZip.extractall()
exampleZip.extract('spam.txt', d)
exampleZip.close()

newZipFileName = d / 'new.bz2'
newZip = zipfile.ZipFile(newZipFileName, 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_BZIP2)
newZip.close()