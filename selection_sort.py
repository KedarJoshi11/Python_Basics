import sys
#function to capture list
def capture_array():
	print("Enter \"done\" when list is compelete. ")
	l1 = []
	while True:
		a = input("Enter element: ")
		if a == "Done" or a == "done" or a == "DONE":
			break
		l1.append(int(a))

	return l1
#function for sorting the list
def selectionSort(array, size):
	for step in range(size):
		min_idx = step

		for i in range(step + 1, size):
			#to sort in descending order, change > to < in this line
			#select the minimum element in each loop
			if array[i] < array[min_idx]:
				min_idx = i

		(array[step], array[min_idx]) = (array[min_idx], array[step])

data = capture_array()
print("The array you entered is: ")
print(data)
size = len(data)
selectionSort(data, size)
print("After performing selection sort on the array. ")
print(data)

