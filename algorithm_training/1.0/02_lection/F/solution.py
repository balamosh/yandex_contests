def CheckSubAnagram(seq, first, last):
    while first < last:
        if seq[first] != seq[last]:
            return False
        first += 1
        last -= 1
    return True

def AppendToAnagram(seq, N):
    last = -1
    for i in range(N):
        if not CheckSubAnagram(seq, i, N - 1):
            last = i
        else:
            break
    ans = []
    for i in range(last + 1):
        ans.insert(0, seq[i])
    print(last + 1)
    if last > 0:
        print(' '.join(list(map(str, ans))))

N = int(input())
seq = list(map(int, input().split()))
AppendToAnagram(seq, N)
