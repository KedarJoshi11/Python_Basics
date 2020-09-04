list1 = []
a = None
oddlist = []

print("Enter numbers or \"quit\" to stop.")
while True:
	a = input(f"Enter number: ")
	if a == 'quit' or a == 'Quit':
		break
	list1.append(a)

print(list1)
print("\n")
print("\nThe odd numbers in the list are: ")

for num in list1:
	if((int(num)%2) != 0):
		oddlist.append(num)

print(oddlist)

