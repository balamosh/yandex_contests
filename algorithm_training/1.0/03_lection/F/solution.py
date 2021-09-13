first = input()
second = input()

second_set = set()
for i in range(len(second) - 1):
    second_set.add(second[i] + second[i + 1])

ans = 0
for i in range(len(first) - 1):
    if first[i] + first[i + 1] in second_set:
        ans += 1
print(ans)
