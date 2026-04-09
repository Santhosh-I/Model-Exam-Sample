import os

path = input("Enter the path: ")

if os.path.isfile(path):
    print("It is a file")
elif os.path.isdir(path):
    print("It is a directory")
else:
    print("Path does not exist")