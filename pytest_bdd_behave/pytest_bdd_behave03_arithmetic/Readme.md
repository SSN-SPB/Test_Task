# Schema of project

project/<br>
│<br>
├── features/<br>
│   ├── arithmetic.feature<br>
│   ├── environment.py # organize import from arithmetic_functions.py <br>
│   └── steps/<br>
│       └── arithmetic_steps.py<br>
├── arithmetic_functions.py # function to test <br>
<br>
# Install library
pip install behave <br>
<br>
# Run test<br>
in root of project run command:<br>
<br>
behave<br>
<br>