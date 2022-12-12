class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.folders = []

    def getSize(self):
        return sum([x.size for x in self.files])

class File:
    def __init__(self, name, parent, file_size):
        self.name = name
        self.parent = parent
        self.size = int(file_size)


folders = []
current_folder = None

with open("input.txt") as file:
    for cmd in file.readlines():

        if cmd.strip().startswith("$ cd"):
            folder_name = cmd.strip().split(" ")[-1]

            if folder_name == "/":
                root = Folder("/", None)
                folders.append(root)
                current_folder = root

            elif folder_name == "..":
                parent = current_folder.parent
                current_folder = parent

            else:
                for folder in current_folder.folders:
                    if folder.name == folder_name:
                        current_folder = folder
                        break

        elif cmd.strip().startswith("$ ls"):
            continue

        elif cmd.strip().startswith("dir"):
            folder = Folder(cmd.strip().split(" ")[-1], current_folder)
            current_folder.folders.append(folder)
            folders.append(folder)

        else:
            size, file_name = cmd.strip().split(" ")
            file = File(file_name, current_folder, size)
            current_folder.files.append(file)


def folder_size(folder):
    f_size = folder.getSize()
    for sub_folder in folder.folders:
        f_size += folder_size(sub_folder)

    return f_size


sum_size = 0
curr_space = folder_size(root)
total_space = 70000000
space_needed = 30000000

deletable_folder_sizes = []

for i in folders:
    s = folder_size(i)
    if s <= 100000:
        sum_size += s

    if s > space_needed - (total_space - curr_space):
        deletable_folder_sizes.append(s)

print(f"Part 1: {sum_size}", f"Part 2: {min(deletable_folder_sizes)}")
