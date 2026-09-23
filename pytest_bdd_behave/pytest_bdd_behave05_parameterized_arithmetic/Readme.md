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
1 behave <br>
2 behave  --format plain  => Separate block for each test like <br>  Given <br>    Then ..<br>
3 behave  --format pretty  => nice format <br>
4 behave  -v  => with Traceback of failed tests<br>
5 behave  --junit  => output to xml at report/*.xml <br>
<br>