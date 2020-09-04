num = input("Enter a number: ")
sum = 0
for i in range(0, (int(num) + 1)):
	if i%3==0 or i%5==0:
		sum += i
print("The sum of the multiples of 3 or 5 upto the number " + str(num) + " is: " + str(sum))