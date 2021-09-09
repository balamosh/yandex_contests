seq_A = list(map(int, input().split()))
seq_B = list(map(int, input().split()))
set_A = set(seq_A)
set_B = set(seq_B)

ans = []
for item in set_A:
    if item in set_B:
        ans.append(item)

print(' '.join(map(str, ans)))
