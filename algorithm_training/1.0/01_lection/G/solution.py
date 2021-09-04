numbers = input().split(' ')
N = int(numbers[0])
K = int(numbers[1])
M = int(numbers[2])

if M > K:
	print(0)
else:
	pieces = 0
	pieces_per_blank = K // M
	left_per_blank = K % M

	while N >= K:
		blanks = N // K
		N = N % K
		N += blanks * left_per_blank
		pieces += blanks * pieces_per_blank

	print(pieces)
