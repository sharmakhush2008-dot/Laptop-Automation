import os

def items_folder(path="."):
    return os.listdir(path)

while True:
    print("=========File System Assistant=========\n")

    print("1. List folder contents")
    print("2. Check if something exists")
    print("3. Create a folder")
    print("4. Find a file.")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        folder = input("Enter the folder path: ")
        if os.path.isdir(folder):
            print(f"Contents of '{folder}':")
            for item in items_folder(folder):
                print(item)
        else:
            print(f"The folder '{folder}' does not exist.")
    elif choice == "2":
        path = input("Enter the path to check: ")
        if os.path.exists(path):
            print(f"The path '{path}' exists.")
        else:
            print(f"The path '{path}' does not exist.")
    elif choice == "3": 
        folder = input("Enter the name of the folder to create: ")
        if not os.path.exists(folder):
            os.mkdir(folder)
            print(f"The folder '{folder}' has been created.")
        else:
            print(f"The folder '{folder}' already exists.")
    elif choice == "4":
        folder = input("Name of the folder you want contents of: ")
        file = input("Name of the file you want to find: ")

        if os.path.exists(folder):

            found = False

            for item in items_folder(folder):
                obj = os.path.join(folder, item)

                if os.path.isfile(obj):
                    if item == file:
                        found = True

            if found:
                print(f"The file '{file}' exists in the folder '{folder}'.")
            
            else:
                print(f"The file '{file}' does not exist in the folder '{folder}'.")

        else:
            print(f"The folder '{folder}' does not exist.")
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

