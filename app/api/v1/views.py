# from .main import app

from models.models import Task
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')

router = APIRouter()
tasks = {}
@router.get('/get')
def get_all_tasks():
    return tasks

@router.get('/get/{id}')
def get_all_tasks(id):
    return tasks[id]

@router.post('/create', response_class=HTMLResponse)
def create_task(task:Task):
    tasks[task.id] = task
    return f'task added successfully {task}'

@router.get("/hello/")
async def hello(request: Request):
    return templates.TemplateResponse('x.html',{"request":request,"name":'Md Abdullah All Mamun'})

# @router.get("/hello/")
# async def hello():
#     ret='''
#     <html>
#         <body>
#             <h2>Hello World!</h2>
#         </body>
#     </html>
#     '''
#     return HTMLResponse(content=ret)