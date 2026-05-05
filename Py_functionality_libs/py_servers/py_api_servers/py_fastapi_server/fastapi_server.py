from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/")
def read_docs():
    return "It is the documentation page for FastAPI server."



@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}