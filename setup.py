import os
import zipfile
import shutil
if os.path.exists("downloads"):
    shutil.rmtree("downloads")
if os.path.exists("sorted"):
    shutil.rmtree("sorted")
os.makedirs("sorted")
os.makedirs("sorted/TV_shows")
os.makedirs("sorted/Movies")
os.makedirs("sorted/unrecognized")
os.makedirs("sorted/audio")
zip = zipfile.ZipFile("downloads.zip")
zip.extractall()
zip.close()