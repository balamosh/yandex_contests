buttons = set(map(int, input().split()))
number_set = set(int(x) for x in input())
ans = 0
for digit in number_set:
    if digit not in buttons:
        ans += 1
print(ans)
