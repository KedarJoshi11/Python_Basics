#function for checking leap year
def isleap(a):
	if a%4==0:
		if a%100 == 0 and a%400 == 0:
			return 1
		elif a%100==0 and a%400 !=0:
			return 0
		else:
			return 1
	else:
		return 0

#taking input
print("This program will print the next 20 leap years")
year = input("Enter an year: ")

#Making sure that the input is acceptable. 
while(year.isdigit() == False):
		print("Wrong Input! Please try again. ")
		year = input("Enter an year: ")
year = int(year)

#Displaying the result if input is a leap year. Then printing the next 20.
if(isleap(year) == 1):
	for i in range(int(year), int(year)+80, 4):
		print(str(i) + " is a leap year.")
elif(isleap(year) == 0):#Finding the next leap year if input is not a leap year. Then printing the next 20.
	for y in range(int(year)+1, int(year)+4):
		if(isleap(y) == 1):
			for i in range(int(y), int(y)+80, 4):
				print(str(i) + " is a leap year.")

