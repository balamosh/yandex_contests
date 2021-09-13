import sys

word_set = set()
for line in sys.stdin:
    for word in line.split():
        word_set.add(word)
print(len(word_set))