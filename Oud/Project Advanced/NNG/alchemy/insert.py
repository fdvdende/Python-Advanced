from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from modelsX.materiaal import Materiaal

engine = create_engine('sqlite:///nng.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Create objects

materiaal = Materiaal('Landingsgestel F16',
                      'Neuswiellandingsgestel',
                      '0023',
                      'landingsgestel',
                      'LG893427',
                      '374589-324678',
                      'front')
session.add(materiaal)

materiaal = Materiaal('Landingsgestel F16',
                      'Hoofdlandingsgestel RA',
                      '0023',
                      'landingsgestel',
                      'LG893428',
                      '374589-324786',
                      'rechtsachter')
session.add(materiaal)

materiaal = Materiaal('Landingsgestel F16',
                      'Hoofdlandingsgestel LA',
                      '0023', 'landingsgestel',
                      'LG893429',
                      '374589-324782',
                      'linksachter')
session.add(materiaal)

materiaal = Materiaal('Landingsgestel F35',
                       'Hoofdlandingsgestel LA',
                       '0023',
                       'landingsgestel',
                       'LG893129',
                       '474589-324782',
                       'front')
session.add(materiaal)

# commit the record the database
session.commit()