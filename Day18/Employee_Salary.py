
class Employee:

  def __init__(self, name, salary_based):
    self.name = name
    self.salary_based = salary_based


  def show_info(self):
    return f"Name: {self.name}, Salary: {self.salary_based}"

  def show_info_p(self):
    print(f"Name: {self.name}, Salary: {self.salary_based}")


  def extra_overtime(self, amount):
    self.salary_based += amount

  def extra_overtime_p(self):
    print(f"Name: {self.name}, Salary: {self.salary_based}")

class Manager(Employee):
  def __init__(self, name, salary_based):
    super().__init__(name, salary_based)

  def manager_info(self):
    mana = super().show_info()
    print(mana)

  def manager_overtime(self, amount):
    super().extra_overtime(amount)
    super().extra_overtime_p()


print("Welcome")

person1 = Employee("Pangya", 1200)
person1.show_info()
person1.extra_overtime(120)
person1.extra_overtime_p()


person2 = Manager("Pangwan", 3000)
person2.manager_info()
person2.manager_overtime(500)
 