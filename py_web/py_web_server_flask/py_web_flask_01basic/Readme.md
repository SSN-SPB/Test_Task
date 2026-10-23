# Project structure
```
flask_training/
│
├── app/
│   ├── __init__.py
│   ├── templates/
│   │   └── data.html
│   │   └── index.html
│   ├── database.py
│   └── routes.py
│
├── database/
│   └── init_db.py
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
docker run --rm --name flask-web-server -p 5000:5000 py-web-flask
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

## DB
### Driver preparation
#### Install and check Drivers
```commandline
python -m pip install pyodbc
python -c "import pyodbc; print(pyodbc.drivers())"
expected output
['SQL Server', 'ODBC Driver 18 for SQL Server', 'Microsoft Access Driver (*.mdb, *.accdb)', 'Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)', 'Microsoft Access Text Driver (*.txt, *.csv)', 'Microsoft Access dBASE Driver (*.dbf, *.ndx, *.mdx)']
```
#### Add Flask and pyodbc into requirements.txt
### Start application with DB
```commandline
$env:DB_PASSWORD = "RequiredPassword"
docker compose up -d
# after that either (preserve data from the previous session)
python .\database\init_db.py
python .\run.py
# or create DB from scratch (losing data from the previous session)
python .\database\reset_db.py --confirm
python .\run.py
```
