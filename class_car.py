class Car:
    def __init__(self, model, year, engine_volume, price, mileage):
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def description(self):
        return (f"Модель: {self.model}, "
                f"Год выпуска: {self.year}, "
                f"Объем двигателя: {self.engine_volume} л, "
                f"Цена: {self.price} РУБ, "
                f"Пробег: {self.mileage} км, "
                f"Количество колес: {self.wheels}")


my_car = Car("Ford Scorpio", 1987, 2.0, 100000, 350000)

print(my_car.description())

class Truck(Car):
    def __init__(self, model, year, engine_volume, price, mileage):
        super().__init__(model, year, engine_volume, price, mileage)
        self.wheels = 8

my_truck = Truck("Атомный КАМАЗ", 2001, 900, 1, 13)

print(my_truck.description())