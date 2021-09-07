def CountPeaks(seq):
    cnt = 0
    for i in range(1, len(seq) - 1):
        if seq[i - 1] < seq[i] and seq[i] > seq[i + 1]:
            cnt += 1
    return cnt

seq = list(map(int, input().split()))
print(CountPeaks(seq))
