N = int(input())

words = set()
stresses = set()
for _ in range(N):
    new_word = input()
    words.add(new_word.lower())
    stresses.add(new_word)

cnt = 0
for word in input().split():
    if word.lower() in words:
        if word not in stresses:
            cnt += 1
        continue
    stress_cnt = sum(1 for c in word if c.isupper())
    if stress_cnt != 1:
        cnt += 1
print(cnt)
