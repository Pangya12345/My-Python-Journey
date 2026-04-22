class Payment:
  def __init__(self, amount):
    self.amount = amount

  def process_payment(self):
    print("Process Payment")

class CreditCard(Payment):
  def __init__(self, amount):
    super().__init__(amount)

  def process_payment(self):
    print(f"Process Payment with CreditCard with the amount of {self.amount}")

class Cryptot(Payment):
  def __init__(self, amount):
    supe().__init__(amount)

  def process_payment(self):
    print(f"Process payment with Cryto with the amount of {self.amount}")
