from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def home():
    return {"user_id": 1003}

@app.get("/shop")
async def shop():
    return {"shop_id": "Food_TP_01"}

if __name__ == '__main__':
    uvicorn.run("03-fastapi-quickstart:app", \
                port=8080, \
                # debug=True, \
                reload=True)