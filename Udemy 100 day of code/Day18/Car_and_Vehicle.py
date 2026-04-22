class Vehicle:
  def __init__(self):
    self.speed = 100
    self.color = "red"

  def move(self):
    return "The vehicle is moving"

class Car(Vehicle):
  def __init__(self):
    super().__init__()

  def car_move(self):
    return f"{self.color} car moving with the speed of {self.speed}"

  def move(self):
    vehicle_move = super().move()
    car_move = self.car_move()
    print(f"{vehicle_move}, {car_move}")


car1 = Car()
car1.move()
