import json


class Person:

    def __init__(self, name, residence):
        self.name = name
        self.residence = residence
        self.kids = []

    def __repr__(self):
        return f'Person("{self.name}", "{self.residence}")'

    def add_kid(self, kid):
        self.kids.append(kid)

    def to_json(self):
        return json.dumps(self, indent=4, default=lambda o: o.__dict__)

    @classmethod
    def from_dict(cls, d):
        name = d['name']
        residence = d['residence']
        p = cls(name, residence)
        for kid in d['kids']:
            k = cls.from_json(kid)
            p.add_kid(k)
        return p

    @classmethod
    def from_json(cls, s):
        return json.loads(s, object_hook = cls.from_dict)




# -----------------------------------------------------

p0 = Person('Peter', 'Lhee')

p1 = Person('Kim', 'Delft')
p1.add_kid(Person('Myra', 'Delft'))
p1.add_kid(Person('Yannick', 'Delft'))
# p0.add_kid(p1)

p2 = Person('Mark', 'Bilthoven')
p2.add_kid(Person('Diego', 'Bilthoven'))
# p0.add_kid(p2)

p3 = Person('Renske', 'Wageningen')
# p0.add_kid(p3)

print(p0)

s = p0.to_json()

print(s)

p = Person.from_json(s)

print('Restored =>', p)