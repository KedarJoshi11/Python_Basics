class BankAccount:
	def __init__(self, name, deposit):
		self.owner = name
		self.balance = deposit

	def getBalance(self):
		return self.balance

	def withdraw(self, amount):
		self.balance -= amount
		return f"New balance is: {self.balance}"

	def deposite(self, amount):
		self.balance += amount
		return f"New balance is: {self.balance}"




name = input("Enter your name: ")
deposit = int(input("Enter the sum you want to deposit: "))
print("Account Created!")

account1 = BankAccount(name, deposit)
print(f"Your account name is: {account1.owner}")
print(f"Your current balance is: {account1.getBalance()}")

amount