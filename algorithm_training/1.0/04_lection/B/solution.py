import sys

word_count = {}
ans = []
for line in sys.stdin:
    for word in line.split():
        if word not in word_count:
            word_count[word] = 0
        else:
            word_count[word] += 1
        ans.append(word_count[word])

print(' '.join(map(str, ans)))
