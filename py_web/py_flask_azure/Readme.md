az login

az webapp up \
  --name web-test-python-smirnov6 \
  --resource-group epmc-tedu \
  --runtime "PYTHON:3.11"

az webapp up --name epmc-tedu-aiplayground-jira-1492-smirnov6 --resource-group epmc-tedu-aiplayground-jira-1492 --runtime "PYTHON:3.11"
D:\a\_work\1\s\build_scripts\windows\artifacts\cli\Lib\site-packages\cryptography/hazmat/backends/openssl/backend.py:8: UserWarning: You are using cryptography on a 32-bit Python on a 64-bit Windows Operating System. Cryptography will be significantly faster if you switch to using a 64-bit Python.
The webapp 'epmc-tedu-aiplayground-jira-1492-smirnov6' doesn't exist
Creating AppServicePlan 'Sergei_Smirnov6_asp_3072' or Updating if already exists
Creating webapp 'epmc-tedu-aiplayground-jira-1492-smirnov6' ...
Configuring default logging for the app, if not already enabled
Creating zip with contents of dir C:\Users\SergeiSmirnov6\Desktop\training_git\private_git\Test_Task\py_web\py_flask_azure ...
Getting scm site credentials for zip deployment
Starting zip deployment. This operation can take a while to complete ...
Warming up Kudu before deployment.
Deployment endpoint responded with status code 202
Polling the status of async deployment. Start Time: 2026-04-28 18:35:20.943082+00:00 UTC
Status: Building the app... Time: 0(s)
Status: Building the app... Time: 17(s)
Status: Building the app... Time: 33(s)
Status: Build successful. Time: 49(s)
Status: Starting the site... Time: 65(s)
Status: Site started successfully. Time: 80(s)
You can launch the app at http://epmc-tedu-aiplayground-jira-1492-smirnov6.azurewebsites.net
Setting 'az webapp up' default arguments for current directory. Manage defaults with 'az configure --scope local'
--resource-group/-g default: epmc-tedu-aiplayground-jira-1492
--sku default: F1
--plan/-p default: Sergei_Smirnov6_asp_3072
--location/-l default: spaincentral
--name/-n default: epmc-tedu-aiplayground-jira-1492-smirnov6
{
  "URL": "http://epmc-tedu-aiplayground-jira-1492-smirnov6.azurewebsites.net",
  "appserviceplan": "Sergei_Smirnov6_asp_3072",
  "location": "spaincentral",
  "name": "epmc-tedu-aiplayground-jira-1492-smirnov6",
  "os": "Linux",
  "resourcegroup": "epmc-tedu-aiplayground-jira-1492",
  "runtime_version": "PYTHON|3.11",
  "runtime_version_detected": "-",
  "sku": "FREE",
  "src_path": "C:\\Users\\..\\py_flask_azure