https://jasmine.github.io/
Jasmine Documentation


powershell (or CL) as admin<br>
1<br>
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

2<br>
npm -v

3<br>
npm install --save-dev jasmine

4<br>
npx jasmine init

5<br>
npm install --save-dev jsdom

6<br>
Run separate test:
<br>
npx jasmine .\spec\dummySpec.js
<br>
Expected: <br>
..<br>
1 spec, 0 failures <br>
<br>
7<br> Run all tests in .\spec
<br>
npx jasmine<br>
(it is defined by .\spec\support\jasmine.json)
<br>
Expected: <br>
..<br>
3 spec, 0 failures <br>
<br>
<h2> Web UI test </h2>

loginUISpec.js (not working yet)

<h3> Need to be installed additionally </h3>
<br> npm init -y
<br> npm install jasmine selenium-webdriver chromedriver
<br> npx jasmine init

npm install chromedriver@136

<br> if needed reinstall:
<br> rm -rf node_modules package-lock.json
<br> npm install
<br> npx jasmine init
