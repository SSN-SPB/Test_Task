<h1> Test Run Flow</h1>
<h2>First, initialize a Node project and install dependencies:</h2>
<br>
<br>npm init -y
<br>
<br>Output
Wrote to C:\Users\SergeiSmirnov6\Desktop\training_git\private_git\Test_Task\jasmine_taf_ui\package.json:
<pre>```js
{
  "name": "jasmine_taf_ui",
  "version": "1.0.0",
  "main": "protractor.conf.js",
  "directories": {
    "test": "tests"
  },
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": ""
}
```</pre>
<br>
<h3>nmp init issue:</h3>
<br>
<br>npm : File C:\Program Files\nodejs\npm.ps1 cannot be loaded because running scripts is disabled on this system. For more <br>information, see 
<br>about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
<br>At line:1 char:1
<br>+ npm init -y
<br>+ ~~~
<br>    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
<br>    + FullyQualifiedErrorId : UnauthorizedAccess
<h4> Resolve as following</h4>
<br>Powershell
<br> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
<br> or permanently:
<br>Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
<br>
<br>
<br>npm install --save-dev protractor jasmine
<br>
<h2>Install Protractor globally to run tests:</h2>
<br>npm install -g protractor
<br>webdriver-manager update
  
To run test:  
jasmine_taf_ui> npx protractor protractor.conf.js  
