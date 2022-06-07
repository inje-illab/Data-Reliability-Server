from fastapi import FastAPI
from .drs import DataExtractor as de, DataQualityManager as dqm, DataTransformer as dt

app = FastAPI()

app.include_router(de.router)
app.include_router(dqm.router)
app.include_router(dt.router)

@app.get("/", tags=["Main"])
async def root():
    return {"hello": "world"}