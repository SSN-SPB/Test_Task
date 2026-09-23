# Project structure
```
flask_training/
│
├── app/
│   ├── __init__.py
│   └── routes.py
│
│
├── requirements.txt
└── run.py
```

# Run
from root CLI run:<br>

python run.py

# Check correctness

## WebUI
1 http://127.0.0.1:5000/api/health
```commandline
{
  "service": "flask-training",
  "status": "ok"
}
```

2 http://127.0.0.1:5000/api/users

```commandline
[
  {
    "id": 1,
    "name": "John"
  },
  {
    "id": 2,
    "name": "Jane"
  },
  {
    "id": 3,
    "name": "Robert"
  }
]
```