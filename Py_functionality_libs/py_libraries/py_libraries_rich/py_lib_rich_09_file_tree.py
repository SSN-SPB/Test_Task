# Rich - is a Python library for rich text and
# beautiful formatting in the terminal.
# It allows you to easily add colors, styles,
# and other formatting options to your terminal output.
# to run use: pip install rich
# python .\py_lib_rich_03_json.py
from rich.tree import Tree
from rich.console import Console

console = Console()

tree = Tree("Project")
src = tree.add("src")
logs = src.add("logs")
logs.add("app.log")
src.add("main.py")
src.add("utils.py")
tree.add("README.md")
tree.add("requirements.txt")

console.print(tree)
