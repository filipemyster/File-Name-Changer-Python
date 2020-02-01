import sys


def main(folderName):
    print(folderName)
    pass


if (__name__ == "__main__") and (len(sys.argv) == 2):
    main(sys.argv[1])
else:
    print("To run the script use: python NameChanger.py <folder_name>")
