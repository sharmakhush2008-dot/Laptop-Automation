import os


def items_folder(path="."):
    return os.listdir(path)


folder = input("Name of the folder you want contents of: ")
if os.path.exists(folder):
    for item in items_folder(folder):
        obj = os.path.join(folder, item)

        if os.path.isfile(obj):
            if item.endswith(".txt"):
                print(item, "- File")
    
        if os.path.isdir(obj):
            print(item, "- Folder")

else:
    os.mkdir(folder)
    print("The folder does not exist.")

