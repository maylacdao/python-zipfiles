# Download dataset from a website and unzip it

import requests
import zipfile

r = requests.get(
    'https://drive.google.com/u/0/uc?id=1dfGerWeWkcyQ9GX9x20rdSGj7WtEpzBB&export=download')

with open('data.zip', 'wb') as f:
    f.write(r.content)

with zipfile.ZipFile('data.zip', 'r') as data_zip:
    print(data_zip.namelist())
    data_zip.extractall('data')

# Points for improvement
# build a scraper for links, then connect this python script with that
# create for loop when dealing with multiple files
