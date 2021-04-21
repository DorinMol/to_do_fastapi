from typing import List
import uuid


class Todo:
    def __init__(self, id: str, title: str, completed: bool):
        self.id = id
        self.title = title
        self.completed = completed


class Todos:
    def __init__(self, todos: List[Todo]):
        self.todos = todos

    def get_by_id(self, id: str):
        filtered = list(filter(lambda todo: str(todo.id) == id, self.todos))
        if filtered:
            return filtered[0]
        return None

    def get_all(self):
        return self.todos

    def delete(self, id: str):
        for i in range(len(self.todos)):
            if str(self.todos[i].id) == id:
                del self.todos[i]
                return "Deleted Sucessfully"
        else:
            return "Id not in the list of todos"

    def add(self, title: str, completed: bool):
        newTodo = Todo(uuid.uuid4(), title, completed)
        self.todos.append(newTodo)
        return newTodo

    def put(self, id: str, completed: bool):
        for todo in self.todos:
            if str(todo.id) == id:
                todo.completed = completed
                return todo
        else:
            return "Todo with specified id doesn't exist"


todos = Todos([
    Todo(uuid.uuid4(), 'Take garbage out', False),
    Todo(uuid.uuid4(), 'Take a shower', False),
    Todo(uuid.uuid4(), 'Learn fastAPI', False)
])
