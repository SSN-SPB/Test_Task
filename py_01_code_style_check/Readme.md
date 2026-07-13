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
