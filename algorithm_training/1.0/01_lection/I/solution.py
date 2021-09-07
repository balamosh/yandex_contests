import itertools

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

brick = [A, B, C]
can_fit = False

for p in itertools.permutations(brick):
	if p[0] <= D and p[1] <= E:
		print("YES")
		can_fit = True
		break
if not can_fit:
	print("NO")
