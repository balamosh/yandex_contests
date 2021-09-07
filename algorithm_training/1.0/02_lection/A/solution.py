def CheckSeq(seq):
    for i in range(len(seq) - 1):
        if seq[i + 1] <= seq[i]:
            return "NO"
    return "YES"

seq = list(map(int, input().split()))
print(CheckSeq(seq))
