# Create Circle class to calculate 'Area' and 'Volume'
class Circle:
  def __init__(self, radius):
    self.radius = radius

  def calculate_area_c(self):
    area_c = 3.14159 * (self.radius ** 2)
    return f"The area of this Circle is {area_c}cm"

  def calculate_volume_c(self):
    volume_c = 4 / 3 * (3.14159 * (self.radius ** 3))
    return f"The volume of this Circle is {volume_c}cm"

# Create Rectangle_Area class to calculate 'Area' of the Rectangle
class Rectangle_Area:
  def __init__(self, lenght, width):
    self.lenght = lenght
    self.width = width

  def calculate_area_r(self):
    area_r = self.width * self.lenght
    return f"The area of this Rectangle is {area_r}cm"

# Create Rectangle_Volume class to calculate 'Volume' of the Rectangle
class Rectangle_Volume(Rectangle_Area):
  def __init__(self, width, lenght, height):
    super().__init__(lenght, width)
    self.height = height

  def calculate_volume_c(self):
    volume = self.height * self.lenght * self.width
    return f"The volume of this Rectangle is {volume}cm"

# Create Triangle_Area class to calculate 'Area' of the Triangle
class Triangle_Area:
  def __init__(self, base, height):
    self.base = base
    self.height = height

  def calculate_area_t(self):
    area_t = 1 / 2 * (self.base * self.height)
    return f"The area of this Triangle is {area_t}cm"

# Create Triangle_volume class to calculate 'Volume' of the Triangle
class Triangle_volume(Triangle_Area):
  def __init__(self, base, height, lenght):
    super().__init__(base, height)
    self.lenght = lenght

  def calculate_volume_t(self):
    volume_t = self.height * self.width * self.lenght
    return f"The volume of this Triangle is {volume_t}cm"



# Game logic
print("Welcome to 'Area' and 'Volume' calculator for Rectangle, Circle and Triangle ")

shape = input("What type of shape do you want to calculate? type 'Rectangle' , 'Circle' or 'Triangle' ").capitalize()
if shape ==  "Circle":
  radius_input = float(input("What is the radius of the Circle? "))
  circle = Circle(radius_input)

elif shape == "Rectangle":
  lenght_input = float(input("What is the lenght of the Rectangle? "))
  width_input = float(input("What is the width of the Rectangle? "))
  rectangle = Rectangle_Area(lenght_input, width_input)


elif shape == "Triangle":
  base = float(input("What is the base of this Triangle? "))
  height = float(input("what is the height of this Triangle? "))
  triangle = Triangle_Area(base, height)

else:
  print("You put the Invalid shape! Try Again!")

type_cal = input("What type of calculation do you want to calculate? type 'Area' or 'Volume' ").capitalize()
if type_cal == "Volume" and shape == "Rectangle":
  height_input = float(input("What is the height of this Rectangle? "))
  rectangle = Rectangle_Volume(lenght_input, width_input, height_input)
  print(rectangle.calculate_volume_r())

elif type_cal == "Volume" and shape == "Triangle":
  lenght_input = float(input("What is the lenght of this Triangle? "))
  triangle = Triangle_volume(base, height, lenght_input)
  print(triangle.calculate_volume_t)

elif type_cal == "Area" and shape == "Rectangle":
  print(rectangle.calculate_area_r())

elif type_cal == "Area" and shape == "Triangle":
  print(triangle.calculate_area_t())

elif type_cal == "Area" and shape == "Circle":
  print(circle.calculate_area_c())

elif type_cal == "Volume" and shape == "Circle":
  print(circle.calculate_volume_c())
