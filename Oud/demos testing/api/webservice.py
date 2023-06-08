from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from todo.todo import ToDo, Status

filename = 'sqlite:///Users/peter/Computrain/_InCompany/Defensie/Python Advanced/demos testing/models/todo.db'
engine = create_engine(filename, echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

app = FastAPI()

@app.get("/")
async def get_all():
    # Select objects
    todo_list = []
    for todo in session.query(ToDo):
        todo_list.append(todo)
    return todo_list

