import sys, re

n, C, D = input().split()
n = int(n)

key_words = set()
for _ in range(n):
    word = input()
    if C == 'no':
        word = word.lower()
    key_words.add(word)

words = {}
first_word_pos = {}
max = 0
max_word = ''
curr_pos = 0
max_pos = -1
for line in sys.stdin:
    str_list = re.split('\W+', line)
    str_list = [x for x in str_list if x and sum(1 for c in x if not x.isdigit())]
    if C == 'no':
        str_list = [x.lower() for x in str_list]
    if D == 'no':
        str_list = [x for x in str_list if not x[0].isdigit()]
    str_list = [x for x in str_list if x not in key_words]
    for i in range(len(str_list)):
        if str_list[i] not in words:
            words[str_list[i]] = 0
            first_word_pos[str_list[i]] = curr_pos
        words[str_list[i]] += 1
        if words[str_list[i]] > max:
            max = words[str_list[i]]
            max_word = str_list[i]
            max_pos = first_word_pos[max_word]
        elif words[str_list[i]] == max and first_word_pos[str_list[i]] < max_pos:
            max_word = str_list[i]
            max_pos = first_word_pos[max_word]
        curr_pos += 1

print(max_word)
