# Создайте класс "Автомобиль", который содержит информацию о марке, модели и
# годе выпуска. Создайте класс "Грузовик", который наследуется от класса
# "Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
# "Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
# информацию о количестве пассажиров

class Automobile:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year

    def get_auto(self):
        return self.mark, self.model, self.year

class Truck(Automobile):
    def __init__(self, mark, model, year, capacity):
        Automobile.__init__(self, mark, model, year)
        self.capacity = capacity

    def get_truck(self):
        return self.mark, self.model, self.year, self.capacity

class Car(Automobile):
    def __init__(self, mark, model, year, capacity_people):
        Automobile.__init__(self, mark, model, year)
        self.capacity_people = capacity_people
    def get_car(self):
        return self.mark, self.model, self.year, self.capacity_people

AutomobileOne = Automobile("Mercedes", "Benz C-W205", 2019)
print(AutomobileOne.get_auto())
AutomobileTwo = Truck("Volvo", "VNL", 2020, 3000)
print(AutomobileTwo.get_truck())
AutomobileThree = Car("Toyota", "Camry", 2021, 5)
print(AutomobileThree.get_car())

