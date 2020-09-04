import math
l1 = []
#function to check if a number is perfect square
def perfect_square(n):
	sr = math.sqrt(int(n))
	if sr.is_integer():
		return True
	else:
		return False
#function for taking a list as an input from the user. 
def take_list():
	print("Enter \"Done\" when over. ")
	while True:
		a = input("Enter the element for your list: ")
		if a == 'Done' or a == 'DONE' or a == 'done':
			break
		l1.append(a)
	return l1

def on_all(l1):
	for i in l1:
		if perfect_square(int(i)):
			print(f"{i} is a perfect square and the 20 perfect square after it are: ")
			root = int(math.sqrt(int(i)))
			#print(root)
			for n in range(int(root), int(root+20)):
				p = n*n
				print(p, end = " ")
			print("\n")
		else:
			print(f"{i} is not a perfect squre. But the 20 perfect square after {i} are: ")
			x = int(i)
			while True:
				x += 1
				if perfect_square(int(x)):
					break
			root = int(math.sqrt(int(x)))
			for n in range(int(root), int(root+20)):
				p = n*n
				print(p, end = " ")
			print("\n")

take_list()
print(f"The list you entered is: {l1}\n")
on_all(l1)
			


