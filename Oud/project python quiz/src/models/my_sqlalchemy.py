from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Rating(Base):
    __tablename__ = 'ranking'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    score = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=False)

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///ranking_sqlachemy.db')

rating = Rating()
