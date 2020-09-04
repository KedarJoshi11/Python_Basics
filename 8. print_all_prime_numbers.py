print("This program prints all prime numbers up to the given limit: ")
limit = input("Enter the number upto which you want prime numbers printed: ")
for number in range(1, int(limit)+1):
	count = 0
	for i in range(2, (number//2+1)):
		if(number%i == 0):
			count = count + 1
			break
	if(count == 0 and number != 1):
		print(str(number) + " is prime. ")