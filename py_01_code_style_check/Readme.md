# Installation

```
python -m py_compile .\your_test_file.py
```

# Correct style black
```
pip install black
black . 
or 
black .\your_test_file.py
or check only:
black --check --diff .
```
## black specific cases
### fix flake8 error like E501 line too long (111 > 79 characters)
```
black . --line-length=79
```

# Library import checking
```
pip install isort
isort .
```


# Check only (flake8)
```
flake8 .
ignore errors
flake8 --ignore=E4,E51,W234
```
## check sourse for specific file
```
flake8 file_name.py --show-source
```