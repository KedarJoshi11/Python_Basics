greet = input("How's it going?")
greet = greet.lower()
stop = 'stop copying me'
while greet != stop:
	print(greet)
	greet = input()
print("UGH Fine, you win. ")