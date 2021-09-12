import sys

word_dict = {}
cnt = 0
ans = ""
for line in sys.stdin:
    words = line.split()
    for i in range(len(words)):
        if words[i] not in word_dict:
            word_dict[words[i]] = 1
        else:
            word_dict[words[i]] += 1
        if word_dict[words[i]] > cnt:
            cnt = word_dict[words[i]]
            ans = words[i]
        elif word_dict[words[i]] == cnt and (words[i] < ans or not ans):
            ans = words[i]
print(ans)
