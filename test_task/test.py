import types

# Старый подход с os.path
import os.path
file_path = os.path.join('data', 'users', 'config.json')
parent_dir = os.path.dirname(file_path)
file_name = os.path.basename(file_path)
print(f"Parent directory: {parent_dir}")
print(f"File name: {file_name}")
print(f"File name: {file_path}")

# Новый подход с pathlib
from pathlib import Path
file_path = Path('data') / 'users' / 'config.json'
parent_dir = file_path.parent
file_name = file_path.name

print(f"Parent directory Path: {parent_dir}")
print(f"File name Path: {file_name}")
print(f"File path Path: {file_path}")