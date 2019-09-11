from fastapi import FastAPI
import api
import uvicorn
from db import init_db

app = FastAPI()

app.include_router(api.router, prefix='/v1')


@app.on_event('startup')
async def initialize_():
    await init_db()

if __name__ == '__main__':
    uvicorn.run(app, **{'host': '0.0.0.0', 'port': 8000})
