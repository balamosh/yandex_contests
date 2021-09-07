def CheckSeq(seq):
    CONSTANT = True
    ASCENDING = True
    WEAKLY_ASCENDING = True
    DESCENDING = True
    WEAKLY_DESCENDING = True
    RANDOM = False

    for i in range(len(seq) - 1):
        if CONSTANT and seq[i] != seq[i + 1]:
            CONSTANT = False
        if ASCENDING and seq[i] >= seq[i + 1]:
            ASCENDING = False
        if WEAKLY_ASCENDING and seq[i] > seq[i + 1]:
            WEAKLY_ASCENDING = False
        if DESCENDING and seq[i] <= seq[i + 1]:
            DESCENDING = False
        if WEAKLY_DESCENDING and seq[i] < seq[i + 1]:
            WEAKLY_DESCENDING = False
        if not CONSTANT and \
           not ASCENDING and \
           not WEAKLY_ASCENDING and \
           not DESCENDING and \
           not WEAKLY_DESCENDING:
            RANDOM = True
            break
    if RANDOM:
        return "RANDOM"
    if CONSTANT:
        return "CONSTANT"
    if ASCENDING:
        return "ASCENDING"
    if DESCENDING:
        return "DESCENDING"
    if WEAKLY_ASCENDING:
        return "WEAKLY ASCENDING"
    if WEAKLY_DESCENDING:
        return "WEAKLY DESCENDING"

seq = []
while True:
    new = int(input())
    if new != -2000000000:
        seq.append(new)
    else:
        break
print(CheckSeq(seq))
