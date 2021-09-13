n = int(input())
w_dict = {}
for _ in range(n):
    w, h = map(int, input().split())
    if w not in w_dict:
        w_dict[w] = h
    elif w_dict[w] < h:
        w_dict[w] = h

ans = 0
for w in w_dict:
    ans += w_dict[w]
print(ans)
