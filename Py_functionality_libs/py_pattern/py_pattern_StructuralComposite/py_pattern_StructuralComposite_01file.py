"""If you're just enforcing method implementation, @abstractmethod is enough,
 but if you're dealing with nested structures
 where both individual and group objects should be treated the same way,
 Composite Pattern is the better approach."""

from abc import ABC, abstractmethod

# Step 1: Define the common interface for Files and Folders
class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self, indent=0):
        pass

# Step 2: Define the Leaf class (File)
class File(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def show_details(self, indent=0):
        print(" " * indent + f"📄 File: {self.name} ({self.size} KB)")

# Step 3: Define the Composite class (Folder)
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def show_details(self, indent=0):
        print(" " * indent + f"📁 Folder: {self.name}")
        for child in self.children:
            child.show_details(indent + 4)

# Step 4: Create a File System Structure
root = Folder("Root")
folder1 = Folder("Documents")
folder11 = Folder("Invoices")
folder2 = Folder("Pictures")

file1 = File("Resume.pdf", 120)
file2 = File("Presentation.ppt", 300)
file3 = File("Photo.jpg", 500)
file4 = File("invoice.txt", 500)

# Build the hierarchy
folder1.add(file1)
folder1.add(file2)
folder1.add(folder11)
folder2.add(file3)
folder11.add(file4)

root.add(folder1)
root.add(folder2)

# Step 5: Display the File System Structure
root.show_details()