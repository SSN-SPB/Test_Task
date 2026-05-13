# Run patch test

from the root of the project, run the following command to execute the patch test:
```python
python -m unittest tests.test_api -v
```
# The expected output should indicate that the test has passed successfully, confirming that the patch has been applied correctly and the functionality is working as intended.
test_get_user (tests.test_api.TestAPI.test_get_user) ... ok
----------------------------------------------------------------------
Ran 1 test in 0.001s