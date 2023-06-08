import jsonpickle
import json

from models.equipment import Equipment
from models.gebeurtenis import Gebeurtenis
from models.onderhoud import Onderhoud
from models.tool import Tool
from models.materiaal import Materiaal

def seed_equipment():
    equipment = Equipment()

    equipment.add_materiaal(Materiaal('Landingsgestel F16', 'Neuswiellandingsgestel', '0023', 'landingsgestel', 'LG893427', '374589-324678', 'front'))
    equipment.add_materiaal(Materiaal('Landingsgestel F16', 'Hoofdlandingsgestel RA', '0023', 'landingsgestel', 'LG893428', '374589-324786', 'rechtsachter'))
    equipment.add_materiaal(Materiaal('Landingsgestel F16', 'Hoofdlandingsgestel LA', '0023', 'landingsgestel', 'LG893429', '374589-324782', 'linksachter'))
    equipment.add_materiaal(Materiaal('Landingsgestel F35', 'Hoofdlandingsgestel LA', '0023', 'landingsgestel', 'LG893129', '474589-324782', 'front'))

    materiaal = equipment.get_materiaal('374589-324678')

    materiaal.add_gebeurtenis( Gebeurtenis('**', '2022-09-05', 'Peter', 'Harde landing', 'Soesterberg', 'windkracht 7 zijwaarts') )
    materiaal.add_gebeurtenis( Gebeurtenis('***', '2022-09-06', 'Peter', 'Zeer harde landing', 'Soesterberg', 'windkracht 7 frontaal') )

    materiaal.add_onderhoudsbeurt( Onderhoud('Inspectie', '2022-09-05', 'Peter', 'OK') )
    materiaal.add_onderhoudsbeurt( Onderhoud('Regulier onderhoud', '2022-09-05', 'Peter', 'OK') )
    materiaal.add_onderhoudsbeurt( Onderhoud('Regulier onderhoud', '2022-08-05', 'Peter', 'OK') )

    materiaal = equipment.get_materiaal('474589-324782')
    materiaal.add_onderhoudsbeurt( Onderhoud('Regulier onderhoud', '2022-05-02', 'Peter', 'OK') )
    materiaal.add_onderhoudsbeurt( Onderhoud('Regulier onderhoud', '2022-06-02', 'Peter', 'OK') )
    materiaal.add_onderhoudsbeurt( Onderhoud('Regulier onderhoud', '2022-07-02', 'Peter', 'OK') )
    materiaal.add_onderhoudsbeurt( Onderhoud('Regulier onderhoud', '2022-08-02', 'Peter', 'OK') )
    materiaal.add_onderhoudsbeurt( Onderhoud('Regulier onderhoud', '2022-09-02', 'Peter', 'OK') )

    print('Data seeded')

    return equipment


if __name__ == '__main__':

    # equipment = seed_equipment()

    try:
        equipment = Equipment.from_pickle()
    except FileNotFoundError:
        equipment = seed_equipment()

    # try:
    #     equipment = Equipment.from_json()
    # except FileNotFoundError:
    #     equipment = seed_equipment()

    equipment.to_pickle()

    # equipment.to_json()

    print(equipment.overzicht())

