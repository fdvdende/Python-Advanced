import os
import pickle

dirname = 'data'

def store(summary, filename):
    with open(os.path.join(dirname, filename), 'wb') as f:
        pickle.dump(summary, f)


def load(filename):
    with open(os.path.join(dirname, filename), 'rb') as f:
        return pickle.load(f)
