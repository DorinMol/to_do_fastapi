from pydantic import BaseModel


class TodoCompleted(BaseModel):
    completed: bool


class TodoModel(TodoCompleted):
    title: str
