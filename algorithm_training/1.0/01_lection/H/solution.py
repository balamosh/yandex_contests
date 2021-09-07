a = int(input())
b = int(input())
n = int(input())
m = int(input())

min_a = n + (n - 1) * a
max_a = n + (n + 1) * a

min_b = m + (m - 1) * b
max_b = m + (m + 1) * b

min_s = max(min_a, min_b)
max_s = min(max_a, max_b)

if min_s > max_s:
	print(-1)
else:
	print(min_s, max_s)
