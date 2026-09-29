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
## from root CLI:
```
python run.py
```

## from docker
```
docker build -t py-web-flask .
docker run --rm -p 5000:5000 py-web-flask
```

# Check correctness

## WebUI
1 Root http://localhost:5000/ <br>
It renders ./templates/index.html
```commandline
Flask Training Application
Health
ok - flask-training
Users
1: John
2: Jane
3: Robert
```



2 http://127.0.0.1:5000/api/health
```
{
  "service": "flask-training",
  "status": "ok"
}
```

3 http://127.0.0.1:5000/api/users

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

## API
```
curl http://localhost:5000/api/health -UseBasicParsing
expect output:
StatusCode        : 200
StatusDescription : OK
Content           : {"service":"flask-training","status":"ok"}

RawContent        : HTTP/1.1 200 OK
                    Connection: close
```
or
```
curl http://localhost:5000/api/users
expect output:
StatusCode        : 200
StatusDescription : OK
Content           : [{"id":1,"name":"John"},{"id":2,"name":"Jane"},{"id":3,"name":"Robert"}]

RawContent        : HTTP/1.1 200 OK
                    Connection: close

```