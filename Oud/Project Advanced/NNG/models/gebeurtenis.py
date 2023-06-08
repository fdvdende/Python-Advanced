import jsonpickle

class Gebeurtenis:

    def __init__(self, intensiteit, datum, betrokken_gebruiker, omschrijving, locatie, omstandigheden):
        self.intensiteit = intensiteit
        self.datum = datum
        self.betrokken_gebruiker = betrokken_gebruiker
        self.omschrijving = omschrijving
        self.locatie = locatie
        self.omstandigheden = omstandigheden

    def __repr__(self):
        return ' - '.join(self.__dict__.values())

    def overzicht(self) -> str:
        return f'{self.datum} - {self.omschrijving}'

    def to_json(self):
        return jsonpickle.dumps(self)

# --------------------------------------------------------------------

if __name__ == '__main__':

    gebeurtenisen = []

    gebeurtenisen.append( Gebeurtenis('**', '2022-09-05', 'Peter', 'Harde landing', 'Soesterberg', 'windkracht 7 zijwaarts') )
    gebeurtenisen.append( Gebeurtenis('***', '2022-09-06', 'Peter', 'Zeer harde landing', 'Soesterberg', 'windkracht 7 frontaal') )

    for gebeurtenis in gebeurtenisen:
        print(gebeurtenis)
