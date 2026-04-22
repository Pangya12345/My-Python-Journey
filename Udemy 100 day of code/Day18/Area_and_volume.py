class Information:
  def __init__(self, width, lenght):
    self.width = width
    self.lenght = lenght

class Area(Information):
  def __init__(self, width, lenght):
    super().__init__(width, lenght)

  def calculate_area(self):
    area = self.width * self.lenght
    return round(area, 2)

  def show_area(self):
    print(f"The Area of the the Rectangle is {self.calculate_area()}cm^2")


class Volume(Information):
  def __init__(self, width, lenght, height):
    super().__init__(width, lenght)
    self.height = height

  def calculate_volume(self):
   volume = self.width * self.lenght * self.height
   return round(volume, 2)

  def show_volume(self):
    print(f"The volume of the Rectangle is {self.calculate_volume()}cm^3")


object1 = Volume(52, 20, 20)
object1.show_volume()

object2 = Area(50, 50)
object2.show_area()
