# Installation

```
pip install pyinstaller
```

# Checking version
```
pyinstaller --version
```


# Create single executable file
```
pyinstaller --onefile SayHello.py
```

## expected output
``` 
│
├── build/
├── dist/
│   └── SayHello.exe
├── SayHello.spec
└── SayHello.py
```

# Run program
```
1 Navigate to dist folder where the executable file is located
2 Open command prompt
3 Then, run the executable file by typing its name and pressing Enter.
```

# Options

## Option One:
Give your program a custom name by using the `--name` option.<br> 
For example, to name your program "MyProgram", you can use the following command:
```
pyinstaller --onefile --name MyProgram SayHello.py
```

## Option Two:
Folder version
```
pyinstaller SayHello.py
```

## expected output
``` 
dist/
└── SayHello/
    ├── SayHello.exe
    ├── python311.dll
    ├── ...

Copy the entire folder if you want to move the application.
```
