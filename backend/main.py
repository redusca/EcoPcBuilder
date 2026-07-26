from fastapi import FastAPI
from endpoints import test_endpoints

app = FastAPI()
app.include_router(test_endpoints.router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "Hello World"}