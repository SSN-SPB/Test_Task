First, initialize the project and install Playwright:    
    
npm init -y    
npm i -D @playwright/test    
npx playwright install 
    
    
npx playwright test    
npx playwright test --headed 
or    

npx playwright test --debug

report:    
npx playwright test --reporter=html 
See report:   
npx playwright show-report    
    