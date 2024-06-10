from fastapi import FastAPI
import uvicorn
from apps.app01 import app01

app = FastAPI()

# parameters
app.include_router(app01, tags=["01 Path"])
app.include_router(app02, tags=["02 Search"])

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)