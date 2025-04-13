Required package installation: 
<br> python -m pip install uvicorn fastapi
<br> Run command: 
<br> <br> python -m uvicorn main:app --reload
<h3> Output of CL</h3>
<br> INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
<br> INFO:     Started reloader process [7468] using StatReload
<br> INFO:     Started server process [17720]
<br> INFO:     Waiting for application startup.
<br> INFO:     Application startup complete.
<br> INFO:     127.0.0.1:62986 - "GET / HTTP/1.1" 200 OK
<br> INFO:     127.0.0.1:62986 - "GET /favicon.ico HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:63045 - "GET /docs HTTP/1.1" 200 OK
<br> INFO:     127.0.0.1:63045 - "GET /openapi.json HTTP/1.1" 200 OK

<h3> Available sites </h3>
<br>Docs UI (Swagger): http://127.0.0.1:8000/docs
<br>Redoc UI: http://127.0.0.1:8000/redoc