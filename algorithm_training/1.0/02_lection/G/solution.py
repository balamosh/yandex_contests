def FindMaxMultiplied(seq):
    min_a = min(seq[0], seq[1])
    min_b = max(seq[0], seq[1])
    max_a = min_b
    max_b = min_a
    for i in range(2, len(seq)):
        if seq[i] < min_a:
            min_b = min_a
            min_a = seq[i]
        elif seq[i] < min_b:
            min_b = seq[i]
        if seq[i] > max_a:
            max_b = max_a
            max_a = seq[i]
        elif seq[i] > max_b:
            max_b = seq[i]
    if max_a * max_b > min_a * min_b:
        return max_b, max_a
    else:
        return min_a, min_b

seq = list(map(int, input().split()))
ans = FindMaxMultiplied(seq)
print(ans[0], ans[1])
