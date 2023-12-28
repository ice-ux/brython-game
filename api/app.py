from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from router.router import turtlerouter
from database.db import userrouter



app = FastAPI()
app.include_router(turtlerouter)
app.include_router(userrouter)
app.mount('/static', StaticFiles(directory='static'),
                       name='static')