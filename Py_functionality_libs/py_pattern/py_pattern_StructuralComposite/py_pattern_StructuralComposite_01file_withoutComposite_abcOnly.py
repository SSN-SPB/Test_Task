from abc import ABC, abstractmethod


# Define the base interface
class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass


# File class (Leaf)
class File(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def show_details(self):
        print(f"📄 File: {self.name} ({self.size} KB)")


# Folder class (No Composite Behavior)
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.files = []  # Only stores files, no nested folders

    def add_file(self, file):
        if isinstance(file, File):  # Explicitly checking the type
            self.files.append(file)
        else:
            raise TypeError("Only File objects can be added!")

    def show_details(self):
        print(f"📁 Folder: {self.name}")
        for file in self.files:
            file.show_details()


# Creating files
file1 = File("Resume.pdf", 120)
file2 = File("Presentation.ppt", 300)

# Creating a folder (can only hold files)
folder = Folder("Documents")
folder.add_file(file1)
folder.add_file(file2)

# Showing details
folder.show_details()

# "How This Differs from the Composite Pattern"
# ❌ Folders cannot contain other folders – only File objects are allowed.
# ❌ Explicit type checking (isinstance(file, File)) – making it less flexible.
# ❌ Limited hierarchy – you cannot have a folder inside another folder.
# ❌ No recursion – show_details() only iterates through files, not subfolders.
# ✅ Still enforces method implementation using @abstractmethod, ensuring consistency.
