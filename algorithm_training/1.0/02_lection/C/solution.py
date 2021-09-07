def FindClosest(seq, x):
    closest = seq[0]
    dist = abs(x - closest)
    for i in range(len(seq) - 1):
        new_dist = abs(x - seq[i + 1])
        if new_dist < dist:
            dist = new_dist
            closest = seq[i + 1]
    return closest

seq = []
N = int(input())
seq = list(map(int, input().split()))
x = int(input())
print(FindClosest(seq, x))
