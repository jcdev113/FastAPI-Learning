from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/items", 
          tags=["item test"],
          summary="item summary",
          description="description of the items"
          )
def test():
    return {"items": "item_data"}


if __name__ == '__main__':
    uvicorn.run("05-paramters-in-decorator:app", \
                port=8080, \
                # debug=True, \
                reload=True)