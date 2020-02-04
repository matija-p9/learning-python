import os

for folder_name in os.listdir():
    if folder_name != "sort-google-photos.py":
        for file_name in os.listdir(folder_name):
            folder__name = folder_name + '/'
            ofile__name = folder__name + file_name
            folder__name = folder__name.replace("/", " ")
            nfile__name = folder__name + file_name
            os.rename(ofile__name, nfile__name)