# Rich - is a Python library for rich text and beautiful formatting in the terminal.
# It allows
# you to easily add colors, styles,
# and other formatting options to your terminal output.
# to run use: pip install rich
# python .\py_lib_rich_03_json.py
from time import sleep
from rich.progress import Progress

with Progress() as progress:
    task = progress.add_task("[cyan]Data treating...", total=100)

    for i in range(100):
        sleep(0.05)
        progress.update(task, advance=1)