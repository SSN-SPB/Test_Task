# Rich - is a Python library for rich text and
# beautiful formatting in the terminal.
# It allows you to easily add colors, styles,
# and other formatting options to your terminal output.
# to run use: pip install rich
# python .\py_lib_rich_03_json.py
from rich.table import Table
from rich.console import Console

console = Console()

table = Table(title="Programming Languages Comparison")

table.add_column("Language", style="bold", justify="left")
table.add_column("Speed", justify="right")
table.add_column("Ease", justify="right")

table.add_row("Python", "Medium", "High")
table.add_row("Rust", "High", "Medium")
table.add_row("C++", "High", "Low")

console.print(table)
