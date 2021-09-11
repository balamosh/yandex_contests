fh = open("input.txt")
lst = list()
for line in fh:
    line = line.rstrip("\n")
lst += line.lower().split()
print(len(set(lst)))
