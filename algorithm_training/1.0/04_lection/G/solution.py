import sys

clients = {}
for line in sys.stdin:
    query = line.split()
    query_type = query[0]
    if query_type == 'DEPOSIT':
        name = query[1]
        sum = int(query[2])
        if name not in clients:
            clients[name] = 0
        clients[name] += sum
    elif query_type == 'WITHDRAW':
        name = query[1]
        sum = int(query[2])
        if name not in clients:
            clients[name] = 0
        clients[name] -= sum
    elif query_type == 'BALANCE':
        name = query[1]
        if name not in clients:
            print('ERROR')
        else:
            print(clients[name])
    elif query_type == 'TRANSFER':
        name1 = query[1]
        name2 = query[2]
        sum = int(query[3])
        if name1 not in clients:
            clients[name1] = 0
        if name2 not in clients:
            clients[name2] = 0
        clients[name1] -= sum
        clients[name2] += sum
    elif query_type == 'INCOME':
        p = int(query[1])
        for client in clients:
            if clients[client] <= 0:
                continue
            add_money = (clients[client] * p) // 100
            clients[client] += add_money
