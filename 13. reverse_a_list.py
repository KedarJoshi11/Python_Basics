list1 = []
n = int(input("Enter the number of elements you want in the list: "))
for i in range(0, n):
	a = int(input(f"Enter the element number {i+1}: "))
	list1.append(a)
print("The list you entered is: \n")
print(list1)
print("\n")
print("The reversed string is: \n")
list1.reverse()
print(list1)
print("\n")

