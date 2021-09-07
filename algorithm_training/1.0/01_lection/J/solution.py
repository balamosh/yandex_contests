a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())
c1 = float(input())
c2 = float(input())

if a1 * b2 != a2 * b1:
	x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
	y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
	print(2, x, y)
else:
	if a1 * c2 != a2 * c1 or b1 * c2 != b2 * c1:
		print(0)
	else:
		if a1 == 0 and b1 == 0:
			if c1 == 0 and a2 == 0 and b2 == 0 and c2 == 0:
				print(5)
			else:
				print(0)
		elif b1 == 0:
			x = c1 / a1
			print(3, x)
		elif a1 == 0:
			y = c1 / b1
			print(4, y)
		else:
			k = -a1 / b1
			b = c1 / b1
			print(1, k, b)
