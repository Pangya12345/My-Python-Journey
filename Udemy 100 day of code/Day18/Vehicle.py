# Define "Ground Vehicle" - CAR
class Car:
  def __init__(self, brand, speed):
    self.speed = speed
    self.brand = brand
    self.wheels = 4
    self.color = "Red"
  
  def vehicle(self):
    return "Car"

  def purpose(self):
    return "Use to drive around"

  def vehicle_type(self):
    return "Automation"

  def full_info(self):
    information1 = {
      "Vehicle": self.vehicle(),
      "Type of Vehicle": self.vehicle_type(),
      "Purpose": self.purpose(),
      "Color": self.color,
      "Brand": self.brand,
      "Wheels": self.wheels,
      "Speed": self.speed
    }
    return information1

# Define "Ground Vehicle" - TRUCK
class Truck(Car):
  def vehicle(self):
    return "Truck"

  def purpose(self):
    return "Use to move heavy objects"

  def vehicle_type(self):
    return "Motor"

# Define "Ground Vehicle (2 wheels)" - MOTORCYCLE
class Motorcycle(Car):
  
  def __init__(self, brand, speed, model, color):
    super().__init__(brand, speed)
    self.model = model
    self.color = color
    self.wheels = 2
    super().full_info()["Model"] = self.model

  def vehicle(self):
    return "Motorcycle"

  def purpose(self):
    return "Efficient travel"

  def vehicle_type(self):
    return super().vehicle_type()

# Define "Ground Vehicle (2 wheels)" - AIRPLANE
class Airplane(Motorcycle):

  def vehicle(self):
    return "Airplane"

  def purpose(self):
    return "Travel around the world"

  def vehicle_type(self):
    return "Wing-Aircraft"

# Define "Ground Vehicle (2 wheels)" - JET
class Jet(Airplane):
      
  def vehicle(self):
    return "Jet"

  def purpose(self):
    return("Long distance travel")

# Define "Water Vehicle" - BOAT
class Boat(Car):
  def __init__(self, brand, speed, model):
    super().__init__(brand, speed)
    self.model = model
    self.color = "Black"
    self.wheels = "No wheels"
  
  def vehicle(self):
    return "Boat"

  def purpose(self):
    return "Travel in the water"

  def vehicle_type(self):
    return "Watercraft"

# Define "Water Vehicle" - JETSKI
class jetski(Boat):

  def vehicle(self):
    return "Jetski"

  def vehicle_type(self):
    return "Personal Watercraft"

# Define "Water Vehicle" - SUBMARINE
class Submarine(Boat):

  def __init__(self, brand, speed, model, depth):
    super().__init__(brand, speed, model)
    self.depth = depth
    super().full_info()["Depth"] = self.depth


  def vehicle(self):
    return "Submarine"

  def purpose(self):
    return "Military Observation"

# Check Full Information for each vehicle
vehicle1 = Car("Toyota", 120)
print(vehicle1.full_info())
print("\n")

vehicle2 = Truck("Volvo", 100)
print(vehicle2.full_info())
print("\n")

vehicle3 = Motorcycle("Susiki", 130, "TG1202", "Grey")
print(vehicle3.full_info())
print("\n")

vehicle4 = Airplane("Bangkok Airways", 980, "A380", "White")
print(vehicle4.full_info())
print("\n")

vehicle5 = Jet("Donald Trump Jet", 1200, "aDonald", "Gold")
print(vehicle5.full_info())
print("\n")


vehicle6 = Boat("Yoat", 80, "AH123")
print(vehicle6.full_info())
print("\n")

vehicle7 = jetski("NATO", 150, "YU6758")
print(vehicle7.full_info())
print("\n")

vehicle8 = Submarine("INTJ", 40, "WU123", "100 Meters")
print(vehicle8.full_info())
print("\n")