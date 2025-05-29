https://jasmine.github.io/
Jasmine Documentation


powershell as admin<br>
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
