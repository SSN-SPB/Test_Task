<h1>Description</h1>
This folder contains Robot Python UI tests</br>
<h2>Preconditions</h2>
<h3>Checked versions:</h3>
Robot Framework 6.0.2 
<br> Python 3.11.1
<h3>Required libraries:</h3>
robotframework==6.0.2
<br> requests==2.28.1
<br> robotframework-selenium2library==3.0.0
<br> robotframework-seleniumlibrary==6.0.0
<br> robotframework-robocop==2.8.1
<br> robotframework-jsonlibrary==0.5
<br> robotframework-pythonlibcore==4.1.2
<br> robotframework-requests==0.9.4
<br>
<br>
<h4>To check libraries run command:</h4>
python -m pip freeze<br>

<h4>Example of run test comand</h4>
robot .\RobotSanityTest.robot<br>
<h2> Code style checking</h2>
Robocop is used
<br> Install robocop command:
<br> pip install robotframework-robocop
<br> 
<h4>Example of run comand:</h4>
robocop .\RobotSanityTest.robot </br>
</html>