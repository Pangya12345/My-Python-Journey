class BankAccount:
  def __init__(self):
    self.account = 0

  def deposit(self, d_amount):
    self.account = self.account + d_amount

  def withdraw(self, w_amount):
    self.account = self.account - w_amount

  def show(self):
    if self.account < 0:
      print("You run out of money")
    else:
      print(f"Balance: {self.account}")


person1 = BankAccount()
person1.deposit(200)
person1.deposit(120)
person1.withdraw(20)
person1.withdraw(300)
person1.show()
