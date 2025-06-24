module.exports = {
  use: {
    headless: false,
    browserName: 'chromium',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
    baseURL: 'https://demoqa.com',
  },
  testDir: './tests',
  retries: 0,
  timeout: 30000,
  // reporter: [['html', { outputFolder: 'playwright-report', open: 'never' }]],
};