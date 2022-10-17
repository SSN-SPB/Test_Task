<h1>Description</h1>
This folder considers the different implementation of testing using python3 and pytest. </br>
Checked with pep8 and pycodestyle.</br>
</br>
Test location - see the ./test/ subdirectory
</br>
<h2>1 Task one</h2>
 tests API for https://www.freeforexapi.com/api/live?pairs= with different pairs of currencies. Each pair is in the separate file</br>
Files</br>
pytest_api_rest_get_task_one.py</br>
pytest_api_rest_get_task_two.py</br>
pytest_api_rest_get_task_three.py</br>
Run expamples:</br>
As pytest: <b><i>pytest -v pytest_api_rest_get_task_one.py</b></i></br>
As python script: <b><i>python pytest_api_rest_get_task_one.py - pytest is ignored in this mode</b></i></br>
</br>
</br>
<h2>2 Example of fixture using within pytest</h2>
File pytest_api_rest_get_task_one_fixture.py</br>
Run:</br>
<b><i>pytest -v -rPf pytest_api_rest_get_task_one_fixture.py</b></i>
</br>
<h2>3 Parameterized pytest run example</h2></br>
File pytest_api_rest_get_tasks_parameterized.py</br>
Run:</br>
<b><i>pytest -vrPf pytest_api_rest_get_tasks_parameterized.py</b></i></br>
</br>
<h2>4 The testing single API request per suite example</h2></br>
File pytest_api_rest_get_singe_request_per_suite.py</br>
Run:</br>
<b><i>pytest -vrPf pytest_api_rest_get_singe_request_per_suite.py</b></i></br>
</br>
<h2>5 Configuration</h2>
<h3>5.1 The default values are defined within /test/pytest.ini</h3></br> 
The running with the default option example is:</br> 
<b><i>pytest test/pytest_api_rest_get_singe_request_per_suite.py</b></i></br></br>  
Possible to run without option:</br>  
<b><i>pytest</b></i> </br> 
Remark: the directory with test files and file mask to select file tor run are defined in the pytest.ini <br>
