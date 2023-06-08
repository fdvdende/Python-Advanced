import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///student.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Select objects
for student in session.query(Student).filter(Student.firstname == 'Eric'):
    print(student.id, student.firstname, student.lastname)