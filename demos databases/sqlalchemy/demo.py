import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///student.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Create objects
for student in session.query(Student).order_by(Student.lastname):
    print(student.id, student.firstname, student.lastname)