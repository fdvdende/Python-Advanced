
class Car:

    metric = 'miles'

    def __init__(self, brand, model, color, mileage = 0):
        self._brand = brand
        self._model = model
        self._color = color
        self._mileage = mileage

    def info(self):
        return f'Car {self._brand} {self._model} {self._color} with mileage {self._mileage} {Car.metric}'

    def drive(self, distance):
        self._mileage += distance

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    @property
    def color(self):
        return self._color

    @property
    def mileage(self):
        return self._mileage

    @classmethod
    def set_metric(cls, new_metric):
        cls.metric = new_metric

    @staticmethod
    def set_metric(new_metric):
        Car.metric = new_metric

    # Factory design pattern
    @staticmethod
    def create_car():
        car = Car('abc', 'xyz', 'red')
        return car


# -----------------------------------

if __name__ == '__main__':

    car = Car('Reanault', 'Megane station', 'brown', 405000)

    print(car.info())

    car.drive(234)

    print(car.info())

    Car.set_metric('mls')

    print(car.info())

    car2 = Car.create_car()
    print(car2.info())
