num = input("Enter a number: ")
sum = 0
for i in range(0, (int(num)+1)):
	sum+=i
print("The sum of numbers upto " + str(num) + " is: " + str(sum))