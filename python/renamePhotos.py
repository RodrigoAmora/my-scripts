#!/usr/bin/python
import os

path = str(raw_input("Digite o ditetorio: "))

namePhotos = str(raw_input("Digite um para as fotos: "))

os.chdir(path)
files =  os.listdir(path)

i = 1

for file in files:
	splitSize = len(file.split("."))
	if file.split(".")[splitSize-1] == "jpg":
		namePhoto = namePhotos+"-%d.jpg"%i
		print file+" -> "+namePhoto
		os.rename(file, namePhoto)
		i = i+1
	if file.split(".")[splitSize-1] == "jpeg":
		namePhoto = namePhotos+"-%d.jpeg"%i
                print file+" -> "+namePhoto
                os.rename(file, namePhoto)
                i = i+1
	if file.split(".")[splitSize-1] == "png":
                namePhoto = namePhotos+"-%d.png"%i
                print file+" -> "+namePhoto
                os.rename(file, namePhoto)
                i = i+1
