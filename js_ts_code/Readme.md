# Install TypeScript
npm install --save-dev typescript

# Check TypeScript
npx tsc --version
```
expected output like:
Version 7.0.2
```
# Convert TypeScript to JavaScript
npx tsc append-word.ts
```
expected that js file is created:
append-word.js
```

# Run TypeScript directly (without converting to JavaScript)
npx tsx append-word.ts

# CodeStyle checking is similar to JavaScript
npx prettier --write .