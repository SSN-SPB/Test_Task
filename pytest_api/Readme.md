This folder considers the different implementation of testing using python3, pytest, pydantic. <br/>
Checked with pep8 and pycodestyle.<br/>
<br/>
<br/>
1 Task one tests API for https://www.freeforexapi.com/api/live?pairs= with different pairs of currencies. Each pair is in the separate file<br/>
pytest_api_rest_get_task_one.py<br/>
pytest_api_rest_get_task_two.py<br/>
pytest_api_rest_get_task_three.py<br/>
Run expamples:<br/>
As pytest: pytest -v pytest_api_rest_get_task_one.py<br/>
As python script: python pytest_api_rest_get_task_one.py - pytest is ignored in this mode<br/>
<br/>
<br/>
2 Checking with pydantic is implemented within: rt_solar_part_one_task_one_pydantic.py.<br/>
Run example: python pytest_api_rest_get_task_one_pydantic.py<br/>
Remark: pep8 checking fails E701 multiple statements on one line (colon) but passes for pycodestyle<br/>
<br/>
<br/>
3 Fixture using within pytest: pytest_api_rest_get_task_one_fixture.py - removed duplicating API call for each test<br/>
Run expamples:<br/>
pytest -v -rPf pytest_api_rest_get_task_one_fixture.py
<br/>
4 Parameterized run example:
pytest_api_rest_get_tasks_parameterized.py
pytest -vrPf pytest_api_rest_get_tasks_parameterized.py
<br/>
4 Part two: find the largest number in the string with special symbols like: grgr$64523424234#54545aaas<br/>
python_largest_two.py - without iteraction<br/>
python_largest_console_version.py - with iteraction in console<br/>