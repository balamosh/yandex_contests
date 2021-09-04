numbers = input().split(' ')
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
d = int(numbers[3])

min_x = max(b, d)
min_y = a + c
min_area = min_x * min_y

x = b + d
y = max(a, c)
area = x * y
if area < min_area:
	min_x = x
	min_y = y
	min_area = area

x = b + c
y = max(a, d)
area = x * y
if area < min_area:
	min_x = x
	min_y = y
	min_area = area

x = max(b, c)
y = a + d
area = x * y
if area < min_area:
	min_x = x
	min_y = y
	min_area = area

print(min_x, min_y)
