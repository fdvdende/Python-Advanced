import json
import os

dirname = 'data'


def store(summary, filename):
    with open(os.path.join(dirname, filename), 'w') as f:
        json.dump(summary, f)

def load(filename):
    with open(os.path.join(dirname, filename), 'r') as f:
        return json.load(f)
