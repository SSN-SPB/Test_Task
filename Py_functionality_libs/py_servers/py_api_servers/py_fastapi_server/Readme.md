# FastAPI Server
Run the following commands in terminal:<br>
python --version<br>
mkdir fastapi-project<br>
cd fastapi-project<br>
python -m venv venv<br>
venv\Scripts\activate<br>
pip install fastapi uvicorn pytest httpx<br>
## Start the server with the following command:<br>
uvicorn fastapi_server:app --reload<br>
<br>
## Open browser:
http://127.0.0.1:8000<br>
It should show:{"message":"Hello, FastAPI!"}<br>
## Swagger docs: 
http://127.0.0.1:8000/docs <br>
It should show the Swagger docs page with the / endpoint and the "Try it out" button. <br>