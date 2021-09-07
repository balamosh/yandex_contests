def FindMaxPlace(seq):
    winner = seq[0]
    could_be_vasily = -1
    for i in range(1, len(seq) - 1):
        if seq[i] % 5 != 0 or seq[i] <= seq[i + 1]:
            if seq[i - 1] > winner:
                winner = seq[i - 1]
                could_be_vasily = -1
            continue
        if seq[i - 1] > winner:
            winner = seq[i - 1]
            if seq[i] <= winner:
                could_be_vasily = seq[i]
            else:
                could_be_vasily = -1
        elif seq[i - 1] == winner:
            if could_be_vasily < seq[i] and seq[i] <= winner:
                could_be_vasily = seq[i]
    if could_be_vasily < 0:
        return 0
    cnt = 0
    for i in range(len(seq)):
        if seq[i] > could_be_vasily:
            cnt += 1
    return cnt + 1

N = int(input())
seq = list(map(int, input().split()))
print(FindMaxPlace(seq))
