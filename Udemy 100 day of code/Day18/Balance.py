# Code Structure (BanlAccount) - "Deposit", "Withdraw", "Show Balance"
def BankAccount():
  Account = 0

  def deposit(d_amount):
    nonlocal Account
    Account = Account + d_amount

  def withdraw(w_amon):
    nonlocal Account
    Account = Account - w_amon
    if Account <= 0:
      print("No money")

  def show():
    print(f"Balance: {Account}")

  return deposit, withdraw, show
d, w, s = BankAccount()

# Decision Space
d(150)
d(300)
w(100)
w(120)
d(500)
s()