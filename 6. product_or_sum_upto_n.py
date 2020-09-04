num = input("Enter a number: ")
op = input("Enter \"+\" for Addition and \"*\" for multiplication: ")
sum = 0
product = 1
if op == "+":
	for i in range(0, (int(num)+1)):
		sum = sum + i
	print("The sum of numbers upto " + str(num) + " is: " + str(sum))
elif op == "*":
	for i in range(1, (int(num)+1)):
		product = product * i
	print("The product of numbers upto " + str(num) + " is: " + str(product))



