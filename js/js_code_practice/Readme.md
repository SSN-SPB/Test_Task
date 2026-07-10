# Run code
node .\filename.js 

# Formatter
Prettier is an opinionated code formatter that automatically formats your code according to its own style, just like black.
<br>
Installation <br>
npm install --save-dev prettier<br>
<br>
or globally <br>
<br>
npm install -g prettier <br>
Format a single file<br>
npx prettier --write example.js<br>
Format all JavaScript files <br>
npx prettier --write "**/*.js" <br>
Check formatting without modifying files <br>
npx prettier --check . <br>