# Abstract Base Class

from abc import ABC, abstractmethod


class Cypher(ABC):

    @abstractmethod
    def encrypt(self, message):
        pass

    @abstractmethod
    def decrypt(self, encrypted):
        pass

