#import dependencies

import zipfile

# METHOD 1 - Manual opening and closing of zip files

# define variable

# my_zip = zipfile.ZipFile('files.zip', 'w')

# write script to create zipfiles

# my_zip.write('test.txt')
# my_zip.write('chalk.jpg')

# my_zip.close()

# METHOD 2 - Using context managers
# context managers - handles opening and closing of files
# compression parameter - to create compressed zip files

with zipfile.ZipFile('files.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write('test.txt')
    my_zip.write('chalk.jpg')
