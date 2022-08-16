<h1>Description</h1>
This folder contains tests examples for Robot test framework REST API tests</br>
<h2>Preconditions</h2>
Checked verions:</br>
Robot Framework 3.2.2 (Python 3.7.4 on win32)</br>
<h2>Required libraries:</h2>
robotframework-jsonlibrary==0.5</br>
robotframework-requests==0.9.3</br>
File Get_Currency_Rate_data.robot verifies the validness the data about currencies that is retrieved via API</br>
<h2>Example of run comand</h2>
robot --include code_check Get_Currency_Rate_data.robot </br>
Example of url: https://www.freeforexapi.com/api/live?pairs=USDRUB</br>
<h2> Code style checking</h2>
Example of run comand: robocop --report rules_by_error_type Get_Currency_Rate_data.robot </br>
</html>
