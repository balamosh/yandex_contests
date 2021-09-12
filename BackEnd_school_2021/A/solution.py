import sys, json

data = json.load(sys.stdin)
data.sort(key=lambda x: x['event_id'])

orders = {}

for event in data:
    order_id = event['order_id']
    item_id = event['item_id']
    count = event['count'] - event['return_count']
    status = event['status']

    if order_id in orders:
        orders[order_id]['items'][item_id] = count
        orders[order_id]['status'][item_id] = status
    else:
        new = {'items': {item_id: count}, 'status': {item_id: status}}
        orders[order_id] = new

formatted_orders = []
for order_id in orders:
    order = orders[order_id]
    item_list = []
    for item_id in order['items']:
        count = order['items'][item_id]
        status = order['status'][item_id]
        if count > 0 and status == 'OK':
            new_item = {}
            new_item['count'] = count
            new_item['id'] = item_id
            item_list.append(new_item)
    if item_list:
        new_dict = {}
        new_dict['id'] = order_id
        new_dict['items'] = item_list
        formatted_orders.append(new_dict)

print(json.dumps(formatted_orders))
