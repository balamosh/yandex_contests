def ListMult(seq):
    ans = 1
    for i in range(len(seq)):
        ans *= seq[i]
    return ans

def MaxTripleMultiplied(seq):
    head = []
    for i in range(3):
        head.append(seq[i])
    head.sort()
    min_trio = head
    max_trio = list(reversed(head))
    for i in range(3, len(seq)):
        if seq[i] < min_trio[0]:
            min_trio[2] = min_trio[1]
            min_trio[1] = min_trio[0]
            min_trio[0] = seq[i]
        elif seq[i] < min_trio[1]:
            min_trio[2] = min_trio[1]
            min_trio[1] = seq[i]
        elif seq[i] < min_trio[2]:
            min_trio[2] = seq[i]
        
        if seq[i] > max_trio[0]:
            max_trio[2] = max_trio[1]
            max_trio[1] = max_trio[0]
            max_trio[0] = seq[i]
        elif seq[i] > max_trio[1]:
            max_trio[2] = max_trio[1]
            max_trio[1] = seq[i]
        elif seq[i] > max_trio[2]:
            max_trio[2] = seq[i]
    if ListMult(max_trio) > min_trio[0] * min_trio[1] * max_trio[0]:
        return max_trio
    else:
        return min_trio[0], min_trio[1], max_trio[0]

seq = list(map(int, input().split()))
ans = MaxTripleMultiplied(seq)
print(ans[0], ans[1], ans[2])
