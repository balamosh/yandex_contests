N = int(input())

x_set = set()
for i in range(N):
    x, y = map(int, input().split())
    x_set.add(x)

print(len(x_set))
