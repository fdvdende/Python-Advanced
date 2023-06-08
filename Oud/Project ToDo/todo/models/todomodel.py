from datetime import datetime
from enum import Enum
import pickle

from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from ..domain.todo import ToDo

filename = 'sqlite:///Users/peter/Computrain/_InCompany/Defensie/Python Advanced/demos testing/models/todo.db'
engine = create_engine(filename, echo=True)
Base = declarative_base()


class ToDoModel(ToDo, Base):
    """"""
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True)
    note = Column(String)
    deadline = Column(String)
    prioriteit = Column(String)
    status = Column(String)
    active = Column(String)

if __name__ == '__main__':
    # create tables
    Base.metadata.create_all(engine)