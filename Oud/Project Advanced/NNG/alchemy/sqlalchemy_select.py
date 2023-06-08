import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from modelsX.materiaal import Materiaal

engine = create_engine('sqlite:///nng.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Create objects
for materiaal in session.query(Materiaal).filter(Materiaal.serienummer=='374589-324786').order_by(Materiaal.naam):
    print(f'{materiaal.serienummer} : {materiaal.naam}')