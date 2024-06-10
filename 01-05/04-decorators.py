from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/get")
def get_test():
    return {"method": "get"}

@app.post("/post")
def post_test():
    return {"method": "post"}

@app.put("put")
def put_test():
    return {"method": "put"}


@app.delete("/delete")
def delete_test():
    return {"method": "delete"}

# @app.patch()
# @app.options()
# @app.head()
# @app.trace()

if __name__ == '__main__':
    uvicorn.run("04-decorators:app", \
                port=8080, \
                # debug=True, \
                reload=True)