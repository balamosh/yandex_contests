n_keys = int(input())
keylife = list(map(int, input().split()))
n_keypresses = int(input())
keypresses = list(map(int, input().split()))

for i in range(n_keypresses):
    keylife[keypresses[i] - 1] -= 1
for i in range(n_keys):
    if keylife[i] < 0:
        print("YES")
    else:
        print("NO")
