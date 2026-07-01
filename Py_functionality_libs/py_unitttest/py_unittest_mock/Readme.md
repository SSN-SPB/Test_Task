# Run patch test

from the root of the project, run the following command to execute the patch test:
```python
python -m unittest .\test_app_ai.py -v
```
# The expected output should indicate that the test has passed successfully, confirming that the patch has been applied correctly and the functionality is working as intended.
```
test_get_user_data_not_found (test_app_ai.TestGetUserData.test_get_user_data_not_found) ... ok
test_get_user_data_success (test_app_ai.TestGetUserData.test_get_user_data_success) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.002s
```