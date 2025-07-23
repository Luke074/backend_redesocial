import uvicorn
from fastapi import FastAPI
from db.postegres import init_db
from db.mongo import mongo_db


app= FastAPI()

@app.get("/", methods=["GET","POST","PUT","DELETE"])
def root():
    init_db()
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)