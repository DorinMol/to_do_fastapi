from fastapi import FastAPI
from app.models import TodoModel as models
from app.data.todos import todos as todo_items

app = FastAPI()


def res(data_to_send):
    return {"data": data_to_send}


@app.get('/')
async def index():
    return res('Use /todos api')


@app.get('/todos')
async def get_todos():
    return res(todo_items.get_all())


@app.get('/todos/{id}')
async def get_todo(id: str):
    return res(todo_items.get_by_id(id))


@app.post('/todos')
async def add_todo(todo: models.TodoModel):
    new_todo = todo_items.add(todo.title, todo.completed)
    return res(new_todo)


@app.delete('/todos/{id}')
async def delete_todo(id: str):
    print(id)
    return res(todo_items.delete(id))


@app.put('/todos/{id}')
async def update(id: str, todo: models.TodoCompleted):
    return res(todo_items.put(id, todo.completed))
