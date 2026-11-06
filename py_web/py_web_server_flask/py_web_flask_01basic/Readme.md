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
# Prepare environment
## DB Driver preparation
#### Install and check Drivers
```commandline
python -m pip install pyodbc
python -c "import pyodbc; print(pyodbc.drivers())"
expected output
['SQL Server', 'ODBC Driver 18 for SQL Server', 'Microsoft Access Driver (*.mdb, *.accdb)', 'Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)', 'Microsoft Access Text Driver (*.txt, *.csv)', 'Microsoft Access dBASE Driver (*.dbf, *.ndx, *.mdx)']
```
#### Add Flask and pyodbc into requirements.txt

# Start application

```commandline
$env:DB_PASSWORD = "RequiredPassword"
1.
docker compose up -d
2. Create and start DB if it is not started yet as follows:
2a. Create DB from scratch (losing data from the previous session)
python .\database\reset_db.py --confirm
or
2b. Create DB preserving data from the previous session
python .\database\init_db.py
3.
python .\run.py
```

### Stop application
```commandline
docker compose down
```


# Check correctness

## WebUI
1 Root http://localhost:5000/ <br>
It renders ./templates/index.html
``` WebUI displays
Flask Training Application
Login
Name: Enter your name

Password: Enter your password
...

```



2 http://127.0.0.1:5000/api/health
``` displays on WebUI
{
  "service": "flask-training",
  "status": "ok"
}
```

3 http://127.0.0.1:5000/api/users

```displays on WebUI
[
{"City":"New York","Email":"john.smith@email.com","FirstName":"John","LastName":"Smith","UserID":1},
{"City":"Chicago","Email":"emma.johnson@email.com","FirstName":"Emma","LastName":"Johnson","UserID":2},
{"City":"Dallas","Email":"michael.brown@email.com","FirstName":"Michael","LastName":"Brown","UserID":3},
{"City":"Seattle","Email":"sophia.davis@email.com","FirstName":"Sophia","LastName":"Davis","UserID":4},
{"City":"Boston","Email":"james.wilson@email.com","FirstName":"James","LastName":"Wilson","UserID":5},
{"City":"Austin","Email":"olivia.taylor@email.com","FirstName":"Olivia","LastName":"Taylor","UserID":6},
{"City":"Denver","Email":"daniel.anderson@email.com","FirstName":"Daniel","LastName":"Anderson","UserID":7}
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
...
```
or
```
curl http://localhost:5000/api/users -UseBasicParsing 
expect output in console:
StatusCode        : 200
StatusDescription : OK
Content           : [{"City":"New York","Email":"john.smith@email.com","FirstName":"John","LastName":"Smith","UserID":1},{"City":"Chicago","Email":"emma.johnson@email.com","FirstName" 
                    :"Emma","LastName":"Johnson","UserID"...
RawContent        : HTTP/1.1 200 OK
                    Connection: close
...
```

