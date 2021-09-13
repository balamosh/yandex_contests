import sys

p_dict = {}
for line in sys.stdin:
    name, item, price = line.split()
    price = int(price)
    if name not in p_dict:
        p_dict[name] = {item: price}
    elif item not in p_dict[name]:
        p_dict[name][item] = price
    else:
        p_dict[name][item] += price

for name in sorted(p_dict.keys()):
    print(name + ':', sep = '')
    for item in sorted(p_dict[name].keys()):
        print(item, p_dict[name][item])
