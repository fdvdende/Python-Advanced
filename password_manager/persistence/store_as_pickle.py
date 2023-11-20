import pickle

filename = '../data/data.pickle'


def store(d):

    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
    except FileNotFoundError:
        data = []

    name = d['name']    # this needs to be and stay unique

    index_to_remove = None
    for i, item in enumerate(data):
        if item['name'] == name:
            index_to_remove = i
            break

    if index_to_remove is None:
        data.append(d)
    else:
        data[index_to_remove] = d

    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def retrieve_one(name):

    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
    except FileNotFoundError:
        data = []

    for item in data:
        if item['name'] == name:
            return item


def retrieve_many(name):
    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
    except FileNotFoundError:
        data = []

    names = []
    for item in data:
        if item['name'].startswith(name):
            names.append(item)

    return names


def get_names():

    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
    except FileNotFoundError:
        data = []

    names = []
    for item in data:
        names.append(item['name'])

    return names
