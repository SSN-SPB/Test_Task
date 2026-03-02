# substring_package

This is a test Python package that provides substring functions.


## Installation
pip install --index-url https://test.pypi.org/simple/ substring_package


## Usage example
```python
from substring_package import substring_by_index, substring_by_index_start_stop
print(substring_by_index("a1b2c3d4e5", 3))
print(substring_by_index_start_stop("a1b2c3d4e5", 3, 7))
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
├── substring-package-0.1.x.tar.gz
└── substring-package-0.1.x-py3-none-any.whl

3 Upload to TestPyPI
```
twine upload --repository testpypi dist/*
```
It should be avaialble at: 
https://test.pypi.org/project/substring-package/0.1.0/
https://test.pypi.org/project/substring-package/0.1.1/
https://test.pypi.org/project/substring-package/0.1.2/


## creating Local installation
Colleague have the following ways to install it:
```
pip install substring_package-0.1.0-py3-none-any.whl
```
or 
```
pip install --index-url https://test.pypi.org/simple/ substring_package
```