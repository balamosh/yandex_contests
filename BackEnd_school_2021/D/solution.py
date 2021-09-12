import csv
 
market, billing = input().split()

billing_file = open(billing)
billing_reader = csv.reader(billing_file)
next(billing_reader)
market_id_set = set()
for row in billing_reader:
    market_id_set.add(int(row[1]))

market_file = open(market)
market_reader = csv.reader(market_file)
offset = len(','.join(next(market_reader))) + 1
market_dict = {}
for row in market_reader:
    id = int(row[0])
    if id in market_id_set:
        market_id_set.remove(id)
        market_dict[id] = offset
    offset += len(','.join(row)) + 1

billing_file.seek(0) 
next(billing_reader)
print('order_id,shop_name,shop_id,cost')
for row in billing_reader:
    market_id = int(row[1])
    if market_id not in market_dict:
        continue
    market_file.seek(market_dict[market_id])
    for m_row in market_reader:
        row.insert(1, m_row[1])
        print(','.join(row))
        break