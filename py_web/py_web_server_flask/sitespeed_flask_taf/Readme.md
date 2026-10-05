# TAF creating for sitespeed.io with Flask
## This repository contains a Test Automation Framework (TAF) for testing sitespeed.io using Flask. The framework is designed to facilitate automated testing of web performance metrics and ensure that web applications meet performance standards.
## ## Features
- Automated testing of web performance metrics using sitespeed.io.
- Integration with Flask for creating web applications and APIs.
- Support for various test scenarios and configurations.
- Detailed reporting of test results and performance metrics.
- ## Getting Started
- ### Prerequisites
- - Python 3.x
- - Flask
- - sitespeed.io
- ### Installation
- npm init -y
- npm install sitespeed.io --save-dev
- #### Checking installation
- To verify that sitespeed.io is installed correctly, run the following command in your terminal:
```bash
node .\node_modules\sitespeed.io\bin\sitespeed.js --version
```
- ## Run tests
- ### Running via node.js CLI

```bash
node .\node_modules\sitespeed.io\bin\sitespeed.js http://127.0.0.1:5000/ -b chrome -n 1
```
#### Expected output for node.js CLI
See file like `sitespeed-result\127.0.0.1\2026-10-05-22-20-32\index.html` for the generated reports. <br>

- ### Running via pytest
- To run the tests, execute the following command in your terminal:
```bash
pytest -v
```

- #### Expected output for pytest
- The test results will be generated in the `reports/sitespeed` directory. <br>
- You can open the `index.html` file in a web browser to view detailed performance metrics and reports.<br>
- ## Contributing
- We welcome contributions to this Test Automation Framework. If you would like to contribute, please follow these steps:
- Fork the repository.
1. Create a new branch for your feature or bug fix.
2. Make your changes and commit them with descriptive messages.
3. Push your changes to your forked repository.
4. Create a pull request to the main repository.
## License
This project is licensed under the MIT License.
