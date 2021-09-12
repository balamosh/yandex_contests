N, M = [int(x) for x in input().split()]
set_A = set()
set_B = set()
for i in range(N):
    set_A.add(int(input()))
for i in range(M):
    set_B.add(int(input()))

common = set()
for item in set_A:
    if item in set_B:
        common.add(item)

unique_A = set()
unique_B = set()
for item in set_A:
    if item not in common:
        unique_A.add(item)
for item in set_B:
    if item not in common:
        unique_B.add(item)
print(len(common))
print(' '.join(map(str, sorted(common))))
print(len(unique_A))
print(' '.join(map(str, sorted(unique_A))))
print(len(unique_B))
print(' '.join(map(str, sorted(unique_B))))
