form = None
sum = 0
for k in range(1, 1000000):
	form = (((-1)**(k+1))/(2*k - 1))*4
	sum = form + sum

print(sum)