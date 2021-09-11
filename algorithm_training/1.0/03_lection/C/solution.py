def insort(seq, item):
    if not seq:
        seq.append(item)
        return seq
    if seq[len(seq) - 1] <= item:
        seq.append(item)
        return seq
    for i in range(len(seq)):
        if seq[i] > item:
            seq.insert(i, item)
            return seq

N, M = [int(x) for x in input().split()]
set_A = set()
set_B = set()
for i in range(N):
    set_A.add(int(input()))
for i in range(M):
    set_B.add(int(input()))

common = []
for item in set_A:
    if item in set_B:
        common = insort(common, item)

unique_A = []
unique_B = []
for item in set_A:
    if item not in set_B:
        unique_A = insort(unique_A, item)
for item in set_B:
    if item not in set_A:
        unique_B = insort(unique_B, item)
print(len(common))
print(' '.join(map(str, common)))
print(len(unique_A))
print(' '.join(map(str, unique_A)))
print(len(unique_B))
print(' '.join(map(str, unique_B)))
