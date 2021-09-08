read = list(map(int, input().split()))
h = read[0]
w = read[1]
mines = read[2]
tab = [[0 for x in range(w)] for y in range(h)]
for mine in range(mines):
    read = list(map(int, input().split()))
    x = read[0] - 1
    y = read[1] - 1
    tab[x][y] = '*'
    left = max(x - 1, 0)
    right = min(x + 2, h)
    down = max(y - 1, 0)
    up = min(y + 2, w)
    for i in range(left, right):
        for j in range(down, up):
            if tab[i][j] != '*':
                tab[i][j] += 1

for line in tab:
    print(' '.join(list(map(str, line))))
