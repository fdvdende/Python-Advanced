import pickle
import jsonpickle
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

from materiaal import Materiaal

class Equipment:

    # FILENAME = r'/Users/peter/Computrain/_InCompany/Defensie/Python Advanced/Project Advanced/NNG/equipment.pickle'

    FILENAME = config['pickle']['filename']

    def __init__(self):
        self.equipment = []

    def add_materiaal(self, materiaal: Materiaal):
        self.equipment.append(materiaal)

    def get_materiaal(self, serienummer: str) -> Materiaal:
        for materiaal in self.equipment:
            if materiaal.serienummer == serienummer:
                return materiaal

    def overzicht(self) -> str:
        s = 'Equipment:\n'
        for materiaal in self.equipment:
            s += str(materiaal) + '\n'
            s += 80 * '=' + '\n'
        return s

    def to_pickle(self):
        with open(Equipment.FILENAME, 'wb') as f:
            pickle.dump(self, f)
            print('Data opgeslagen in equipment.pickle')

    @staticmethod
    def from_pickle():
        try:
            with open(Equipment.FILENAME, 'rb') as f:
                equipment = pickle.load(f)
                print('Data gelezen uit equipment.pickle')
                return equipment
        except FileNotFoundError:
            print('Kan het bestand niet vinden')
            raise FileNotFoundError()

    def to_json(self):
        s = jsonpickle.dumps(self)
        with open('equipment.json', 'w') as f:
            f.write(s)
            print('Data opgeslagen in equipment.json')

    @staticmethod
    def from_json():
        try:
            with open('equipment.json', 'r') as f:
                s = f.read()
                equipment = jsonpickle.loads(s)
                print('Data gelezen uit equipment.pickle')
                return equipment
        except FileNotFoundError:
            print('Kan het bestand niet vinden')
            raise FileNotFoundError()


# ----------------------------

if __name__ == '__main__':

    equipment = Equipment()

    equipment.add_materiaal(Materiaal('Landingsgestel F16', 'Neuswiellandingsgestel', '0023', 'landingsgestel', 'LG893427', '374589-324678', 'front'))
    equipment.add_materiaal(Materiaal('Landingsgestel F16', 'Hoofdlandingsgestel RA', '0023', 'landingsgestel', 'LG893428', '374589-324786', 'rechtsachter'))
    equipment.add_materiaal(Materiaal('Landingsgestel F16', 'Hoofdlandingsgestel LA', '0023', 'landingsgestel', 'LG893429', '374589-324782', 'linksachter'))
    equipment.add_materiaal(Materiaal('Landingsgestel F35', 'Hoofdlandingsgestel LA', '0023', 'landingsgestel', 'LG893129', '474589-324782', 'front'))
