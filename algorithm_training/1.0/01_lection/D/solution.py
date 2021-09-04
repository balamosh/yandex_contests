a = int(input())
b = int(input())
c = int(input())

if c < 0:
	print("NO SOLUTION")
elif a == 0:
	if b == c * c:
		print("MANY SOLUTIONS")
	else:
		print("NO SOLUTION")
else:
	ax = c * c - b
	if ax % a == 0:
		print(ax // a)
	else:
		print("NO SOLUTION")
