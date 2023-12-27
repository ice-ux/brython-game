from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'),
          name='static')


# 设置模板存放路径
template = Jinja2Templates(directory='templates')

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/turtle")
async def read_turtle(request: Request): # async加了就支持异步  把Request赋值给request
    return template.TemplateResponse('index.html',{'request': request})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host='127.0.0.1', port=9099)