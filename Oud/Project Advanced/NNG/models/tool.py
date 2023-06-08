import jsonpickle

class Tool:

    def __init__(self, soort, serienr):
        self.soort = soort
        self.serienr = serienr

    def __repr__(self):
        return ' - '.join(map(str, self.__dict__.values()))

    def to_json(self):
        return jsonpickle.dumps(self)


# ---------------------------------------------

if __name__ == '__main__':

    tooling = []

    tooling.append( Tool('Steeksleutel 10', '34534534') )
    tooling.append( Tool('Steeksleutel 12', '34534523') )
    tooling.append( Tool('Schoevedraaier Philips', '345345') )

    for tool in tooling:
        print(tool)

