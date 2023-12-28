from starlette.templating import Jinja2Templates
from starlette.requests import Request
from fastapi import APIRouter, Depends, HTTPException

# from ..dependencies import get_token_header  # 通过 .. 对依赖项使用了相对导入，具体代码可看第二章

turtlerouter = APIRouter(
    prefix="/turtle",
    tags=["turtle"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


# 设置模板存放路径
template = Jinja2Templates(directory='templates')

@turtlerouter.get("/")
async def read_turtle(request: Request): # async加了就支持异步  把Request赋值给request
    return template.TemplateResponse('index.html',{'request': request})