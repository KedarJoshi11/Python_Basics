def square(num):
	result = num * num
	return result

num = int(input("Enter the number you want the square of: "))
print(square(num))
num = int(input("Enter the number you want the square of: "))
print(square(num))

print("Now let's look at Addition function.")

def add(a, b):
	result = a + b
	return result

a = int(input("Enter the first number to add: "))
b = int(input("Enter the second number to add: "))

print(f"The addition of {a} and {b} is: {add(a, b)}")

print("Now let's look at multiplication")

def multiply(x, y):
	result = x * y
	return result

x = int(input("Enter the first number to multiply: "))
y = int(input("Enter the second number to add: "))
print(f"The multiplication of {x} and {y} is {multiply(x, y)}")


def divide(num1, num2):
	result = num1/num2
	return result

num1 = int(input("Enter the numerator: "))
num2 = int(input("Enter the denomincator: "))
print(f"The division of {num1} and {num2} is {divide(num1, num2)}")

def exponent(number, power):
	result = number ** power
	return result

number = int(input("Enter the number: "))
power = int(input("Enter the power: "))
print(f"{number} to the power {power} is: {exponent(number, power)}")