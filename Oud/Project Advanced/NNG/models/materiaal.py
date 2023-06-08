import jsonpickle

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///nng.db', echo=True)
Base = declarative_base()

from gebeurtenis import Gebeurtenis
from onderhoud import Onderhoud

class Materiaal(Base):
    """Dit is mijn Materiaal klasse. Het gaat om een een enkel stuk materiaal."""

    __tablename__ = "materiaal"

    id = Column(Integer, primary_key=True)
    naam = Column(String)
    omschrijving = Column(String)
    atacode = Column(String)
    soort = Column(String)
    partnummer = Column(String)
    serienummer = Column(String)
    positie = Column(String)

    def __init__(self, naam, omschrijving, atacode, soort, partnummer, serienummer, positie):
        self.naam = naam
        self.omschrijving = omschrijving
        self.atacode = atacode              # eg 23
        self.type = soort
        self.partnummer = partnummer
        self.serienummer = serienummer
        self.positie = positie
        self.gebeurtenissen = []
        self.onderhoudsbeurten = []

    def __repr__(self) -> str:
        return ' - '.join(map(str, self.__dict__.values()))

    def add_gebeurtenis(self, gebeurtenis: Gebeurtenis):
        """Koppel een gebeurtenis aan dit materiaal

        Params:
            gebeurtenis - een severe gebeurtenis"""
        self.gebeurtenissen.append(gebeurtenis)

    def add_onderhoudsbeurt(self, onderhoudsbeurt: Onderhoud):
        """Koppel een onderhoudsbeurt aan dit materiaal

        Params:
            onderhoudsbeurt - een onderhoudsbeurt"""
        self.onderhoudsbeurten.append(onderhoudsbeurt)

    def overzicht(self) -> str:
        s = f'{self.serienummer} - {self.naam}\n'
        if self.gebeurtenissen:
            s += 'Gebeurtenissen:\n'
            for gebeurtenis in self.gebeurtenissen:
                s += gebeurtenis.overzicht() + '\n'
        if self.onderhoudsbeurten:
            s += 'Onderhoudsbeurten:\n'
            for onderhoudsbeurt in self.onderhoudsbeurten:
                s += onderhoudsbeurt.overzicht() + '\n'
        return s

    def to_json(self):
        return jsonpickle.dumps(self)

# --------------------------------------------------------------------

if __name__ == '__main__':

    # create tables
    Base.metadata.create_all(engine)

    # materieel = []
    #
    # materieel.append( Materiaal('Landingsgestel F16', 'Neuswiellandingsgestel', '0023', 'landingsgestel', 'LG893427', '374589-324678', 'front') )
    # materieel.append( Materiaal('Landingsgestel F16', 'Hoofdlandingsgestel RA', '0023', 'landingsgestel', 'LG893428', '374589-324786', 'rechtsachter') )
    # materieel.append( Materiaal('Landingsgestel F16', 'Hoofdlandingsgestel LA', '0023', 'landingsgestel', 'LG893429', '374589-324782', 'linksachter') )
    # materieel.append( Materiaal('Landingsgestel F35', 'Hoofdlandingsgestel LA', '0023', 'landingsgestel', 'LG893129', '474589-324782', 'front') )
    #
    # for materiaal in materieel:
    #     if 'F16' in materiaal.naam:
    #         print(materiaal)
    #
    # for materiaal in materieel:
    #     if materiaal.serienummer == '374589-324678':
    #         found_materiaal = materiaal
    #         break
    #
    # found_materiaal.add_gebeurtenis( Gebeurtenis('**', '2022-09-05', 'Peter', 'Harde landing', 'Soesterberg', 'windkracht 7 zijwaarts') )
    # found_materiaal.add_gebeurtenis( Gebeurtenis('***', '2022-09-06', 'Peter', 'Zeer harde landing', 'Soesterberg', 'windkracht 7 frontaal') )
    # found_materiaal.add_gebeurtenis( Gebeurtenis('**', '2022-09-05', 'Peter', 'Harde landing', 'Soesterberg', 'windkracht 7 zijwaarts') )
    #
    # print(found_materiaal)
    #
