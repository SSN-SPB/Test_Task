# Rich - is a Python library for rich text and beautiful formatting in the terminal.
# It allows
# you to easily add colors, styles,
# and other formatting options to your terminal output.
# to run use: pip install rich
# python .\py_lib_rich_03_json.py
from rich.console import Console
from rich.json import JSON

console = Console()

# Пример JSON-данных
data = '{"name": "Python3", "type": "Programming Language", "year": 2008}'

# Форматированный вывод JSON
console.print(JSON(data))