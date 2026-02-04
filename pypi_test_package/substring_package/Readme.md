# substring_package

This is a test Python package that provides substring functions.


## Installation
pip install --index-url https://test.pypi.org/simple/ substring_package


## Usage example
```python
from substring_package import substring_by_index
print(substring_by_index("a1b2c3d4e5", 3))
```

## Package creating
```
pip install --upgrade build twine
```

Remark:
build → creates distribution files
twine → uploads them to PyPI)

2 build (within directory 'substring_package')
```
python -m build
```
This command creates
dist/
├── coolmath-0.1.0.tar.gz
└── coolmath-0.1.0-py3-none-any.whl

3 Upload to TestPyPI
```
twine upload --repository testpypi dist/*
```
It should be avaialble at: https://test.pypi.org/project/substring-package/0.1.0/


## creating Local installation
Colleague have the following ways to install it:
```
pip install substring_package-0.1.0-py3-none-any.whl
```
or 
```
pip install --index-url https://test.pypi.org/simple/ substring_package
```