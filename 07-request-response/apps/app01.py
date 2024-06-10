from fastapi import APIRouter

app01 = APIRouter()

## render in order...
@app01.get("/user/1")
def get_user():
    return {"user_id":"root user"}

@app01.get("/user/{uid}")
def get_user(uid):
    print("id", uid)
    return {"user_id":uid}

@app01.get("/article/{id}")
def get_article(id:int):
    print("id", id)
    return {"article_id":id}