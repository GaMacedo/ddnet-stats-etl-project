from zipfile import ZipFile
import os
import shutil

'''
This file is to extract the csv files from the zip downloaded previously
'''

file_path = 'data/stats.zip'

# Extract all files from zip
with ZipFile(file_path, 'r') as zipObj:
    listOfFileNames = zipObj.namelist()
    zipObj.extractall(path='data/', members=listOfFileNames)

# Move all files to Data directory
path = 'data/ddnet-stats/'
new_path = 'data/'
files = os.listdir('data/ddnet-stats')
for file in files:
    if file.endswith('.csv'):
        shutil.move(path + file, new_path + file)

# Remove the old directory
os.rmdir(path)

# Remove zip file
os.remove(file_path)
