import os.path
import urllib.parse
import configparser
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..models.todomodel import ToDoModel

config = configparser.ConfigParser()
config.read('config.ini')

project_directory = os.path.dirname(os.path.abspath(__name__))
project_directory = os.getcwd()
filename = os.path.join(project_directory, config['sqlite']['database'])
# filename = urllib.parse.quote_plus(os.path.join(project_directory, config['sqlite']['database']))

print(filename)

engine = create_engine('sqlite:////' + filename, echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

app = FastAPI()

@app.get("/")
def get_all():
    return 'api'
     # Select objects
    # todo_list = []
    # for todo in session.query(ToDoModel):
    #     todo_list.append(todo)
    # return todo_list

