size = int(input())

synonyms = {}
for _ in range(size):
    first, second = input().split()
    synonyms[first] = second
    synonyms[second] = first

word = input()
print(synonyms[word])
