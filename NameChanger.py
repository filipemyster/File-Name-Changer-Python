import sys
from os import listdir, path, rename
from os.path import isfile, join
from random import randrange


def main(folderName):
    if not path.exists(folderName):
        print("The folder " + str(folderName) + " was not found.")
        return

    # Process the files in the folder
    files = [f for f in listdir(folderName) if isfile(join(folderName, f))]

    print("Found " + str(len(files)) + " files in the folder.")
    for f in files:
        changeName(folderName, f)
    pass


def changeName(folderName, fileName):
    suffix = randrange(0, 1000000)

    oldFile = folderName + "/" + fileName
    newFile = folderName + "/" + str(suffix) + "_" + fileName
    rename(oldFile, newFile)
    pass


if (__name__ == "__main__") and (len(sys.argv) == 2):
    main(sys.argv[1])
else:
    print("To run the script use: python NameChanger.py <folder_name>")
