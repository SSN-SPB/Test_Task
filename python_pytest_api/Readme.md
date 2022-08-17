<h1>Description</h1>
This folder considers the different implementation of testing using python3, pytest, pydantic. </br>
Checked with pep8 and pycodestyle.</br>
</br>
</br>
1 Task one tests API for https://www.freeforexapi.com/api/live?pairs= with different pairs of currencies. Each pair is in the separate file</br>
pytest_api_rest_get_task_one.py</br>
pytest_api_rest_get_task_two.py</br>
pytest_api_rest_get_task_three.py</br>
Run expamples:</br>
As pytest: pytest -v pytest_api_rest_get_task_one.py</br>
As python script: python pytest_api_rest_get_task_one.py - pytest is ignored in this mode</br>
</br>
</br>
2 Fixture using within pytest: pytest_api_rest_get_task_one_fixture.py - removed duplicating API call for each test</br>
Run expamples:</br>
pytest -v -rPf pytest_api_rest_get_task_one_fixture.py
</br>
3 Parameterized pytest run example:</br>
pytest_api_rest_get_tasks_parameterized.py</br>
pytest -vrPf pytest_api_rest_get_tasks_parameterized.py</br>
</br>
4 The testing single API request example: </br>
pytest -vrPf pytest_api_rest_get_task_one_singe_api.py</br>
