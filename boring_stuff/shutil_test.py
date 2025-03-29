import shutil, os
from pathlib import Path
import sys
import send2trash

# p=Path.home()
# print(p)

p=Path.cwd()
print(p)

d = Path(p / 'somefolder')
if not d.exists():
    os.mkdir(d)
if not d.is_dir():    
    print(f'{d} is not directory' )
    sys.exit() 
shutil.copy(p / 'shutil_test.py', d)
shutil.copy(p / 'shutil_test.py', d / 'test.py')
# shutil.rmtree(d)
send2trash.send2trash(d)

folderCount = 0
fileCount = 0
# for folderName, subfolders, filenames in os.walk(Path.home()):
for folderName, subfolders, filenames in os.walk('D:\\prog\\react'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        folderCount += 1
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
        fileCount += 1
    print('')

print(f'Folder count={folderCount} File count={fileCount}')