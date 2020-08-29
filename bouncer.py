#ask for age
#print("What is your age: ")
age = input("What is your age: ")

if age:
	age = int(age)
	if age >= 18 and age < 21:
		print("You can go, but please wear the wristband.")
	elif int(age) > 21:
		print("You can go and have fun!")
	else:
		print("You are a kid, go home.")
else:
	print("Please don't forget entering an age!")
