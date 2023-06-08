from datetime import datetime
from enum import Enum
import pickle

class Status(Enum):
    TODO = 1
    STARTED = 2
    WAITING = 3
    DONE = 4


class ToDo:

    def __init__(self,
                 note: str,
                 deadline: datetime = None,
                 prioriteit: int = 0,
                 status: Status = Status.TODO,
                 active: bool = True):
        self._note = note
        self._deadline = deadline
        self._prioriteit = prioriteit
        self._status = status
        self._active = active
        self._created = datetime.now()

    def __repr__(self):
        return f'ToDo("{self.note}", {self.deadline}, {self.prioriteit}, {self.status}, {self.active})'

    def __str__(self):
        s = 'ToDo:\n'
        # s += '\n'.join(f'{k:16} : {v}' for k, v in self.__dict__.items())
        for k, v in self.__dict__.items():
            s += f'{k:16} : {v}\n'
        return s.rstrip('\n')

    def save(self, filename = 'user.pickle'):
        with open(filename, 'wb') as f:
            pickle.dump(self.__dict__, f)

    def load(self, filename = 'user.pickle'):
        with open(filename, 'rb') as f:
            self.__dict__.update(pickle.load(f))

    @staticmethod
    def restore(filename = 'user.pickle'):
        o = ToDo('_')
        with open(filename, 'rb') as f:
            o.__dict__.update(pickle.load(f))
        return o

    @property
    def note(self):
        return self._note

    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, value):
        self._deadline = value

    @property
    def prioriteit(self):
        return self._prioriteit

    @prioriteit.setter
    def prioriteit(self, value):
        self._prioriteit = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value

    @property
    def created(self):
        return self._created


if __name__ == '__main__':

    todo = ToDo('Boodschappen doen')

    print(str(todo))
    print(repr(todo))

    # todo.save()

    # todo.load()
    #
    # print(str(todo))
    # print(repr(todo))
    #
    # todo2 = ToDo.restore()
    #
    # print(str(todo2))
    # print(repr(todo2))

    # print({item.name: item for item in list(Status)})
