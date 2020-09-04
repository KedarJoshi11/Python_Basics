print("The program tests if the string you entered is a palindrome or not. \n")
print("Enter \"done\" when you want to stop. ")
a = None
r = None

while True:
	a = input("Enter a string: ")
	a.lower()
	if a == 'done':
		break
	b = a[::-1]

	if b == a:
		print("The string is a palindrome")
	else:
		print("Not a palindrome")



