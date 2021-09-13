g, len_S = map(int, input().split())
W = input()
S = input()
len_W = len(W)

W_dict = {}
S_curr_dict = {}

for i in range(ord('a'), ord('z') + 1):
    W_dict[chr(i)] = 0
    S_curr_dict[chr(i)] = 0
for i in range(ord('A'), ord('Z') + 1):
    W_dict[chr(i)] = 0
    S_curr_dict[chr(i)] = 0

for i in range(len_W):
    W_dict[W[i]] += 1
    S_curr_dict[S[i]] += 1

cnt = 0
if W_dict == S_curr_dict:
    cnt += 1
first = 0
for i in range(len_W, len_S):
    S_curr_dict[S[i]] += 1
    S_curr_dict[S[first]] -= 1
    first += 1
    if W_dict == S_curr_dict:
        cnt += 1

print(cnt)
