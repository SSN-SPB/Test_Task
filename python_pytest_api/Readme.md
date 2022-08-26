<h1>Description</h1>
This folder considers the different implementation of testing using python3 and pytest. </br>
Checked with pep8 and pycodestyle.</br>
</br>
</br>
<h2>1 Task one</h2>
 tests API for https://www.freeforexapi.com/api/live?pairs= with different pairs of currencies. Each pair is in the separate file</br>
Files</br>
pytest_api_rest_get_task_one.py</br>
pytest_api_rest_get_task_two.py</br>
pytest_api_rest_get_task_three.py</br>
Run expamples:</br>
As pytest: pytest -v pytest_api_rest_get_task_one.py</br>
As python script: python pytest_api_rest_get_task_one.py - pytest is ignored in this mode</br>
</br>
</br>
<h2>2 Example of fixture using within pytest</h2>
File pytest_api_rest_get_task_one_fixture.py</br>
Run expamples:</br>
pytest -v -rPf pytest_api_rest_get_task_one_fixture.py
</br>
<h2>3 Parameterized pytest run example</h2></br>
File pytest_api_rest_get_tasks_parameterized.py</br>
Run expamples:</br>
pytest -vrPf pytest_api_rest_get_tasks_parameterized.py</br>
</br>
<h2>4 The testing single API request per suite example</h2></br>
File pytest_api_rest_get_singe_request_per_suite.py</br>
Run expamples:</br>
pytest -vrPf pytest_api_rest_get_singe_request_per_suite.py</br>
</br>