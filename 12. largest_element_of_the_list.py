list1 = [] #creating an empty list
a = None # creating a variable that contains nothing yet
n = int(input("Enter the numbers of elements you want in your list: "))

#taking input in the list
for i in range(0, n):
	a = int(input(f"Enter element number {i+1}: "))
	list1.append(a)
print("\n")
print(list1)
print("\n")

#using the max() method to find the largest number
largest = max(list1)
print(f"The largest number in the list is: {largest}")
print("\n")

