import jsonpickle

class Onderhoud:

    def __init__(self, naam, datum, door_wie, bevindingen):
        self.type = naam
        self.datum = datum
        self.door_wie = door_wie
        self.bevindingen = bevindingen
        self.onderdelen = []
        self.verbruiksmiddelen = []
        self.tooling = []

    def __repr__(self):
        return ' - '.join(map(str, self.__dict__.values()))

    def add_onderdeel(self, onderdeel):
        self.onderdelen.append(onderdeel)

    def add_verbruiksmiddel(self, verbruiksmiddel):
        self.verbruiksmiddelen.append(verbruiksmiddel)

    def add_tool(self, tool):
        self.tooling.append(tool)

    def overzicht(self) -> str:
        return f'{self.datum} - {self.type}'

    def to_json(self):
        return jsonpickle.dumps(self)

# --------------------------------------------------------------------

if __name__ == '__main__':

    from tool import Tool

    onderhoudsbeurten = []

    onderhoudsbeurten.append( Onderhoud('Inspectie', '2022-09-05', 'Peter', 'OK') )
    onderhoudsbeurten.append( Onderhoud('Regulier onderhoud', '2022-09-05', 'Peter', 'OK') )
    onderhoudsbeurten.append( Onderhoud('Regulier onderhoud', '2022-08-05', 'Peter', 'OK') )

    onderhoud = Onderhoud('Spoed onderhoud', '2022-08-15', 'Peter', 'OK')
    onderhoud.add_tool( Tool('Steeksleutel 10', '34534534') )
    onderhoud.add_tool( Tool('Steeksleutel 12', '34534523') )
    onderhoud.add_tool( Tool('Schoevedraaier Philips', '345345') )
    onderhoudsbeurten.append( onderhoud )

    for onderhoud in onderhoudsbeurten:
        bFound = False
        for tool in onderhoud.tooling:
            if tool.serienr == '345345':
                bFound = True
        if bFound:
            print(onderhoud)

