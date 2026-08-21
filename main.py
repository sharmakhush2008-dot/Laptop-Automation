import os

def list_folder(path="."):
    """Return a list of names in the given folder."""
    return os.listdir(path)


if __name__ == "__main__":
    folder = "."
    items = list_folder(folder)
    for item in items:
        print(item)