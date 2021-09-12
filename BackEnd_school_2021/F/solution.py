n, m = map(int, input().split())

curr_cache_size = 0
cache = {}

ans = []

id, time = input().split()
time = int(time)
cache[id] = time
curr_cache_size += 1
new = ['1', 'PUT', id]
ans.append(new)

min_key = id
min_value = time

for i in range(2, n + 1):
    id, time = input().split()
    time = int(time)
    if id in cache and cache[id] < time:
        cache[id] = time
        if id == min_key:
            min_key = min(cache, key=cache.get)
            min_value = cache[min_key]
        new = [str(i), 'UPDATE', id]
        ans.append(new)
        continue
    if id not in cache:
        if curr_cache_size == m:
            if cache[min_key] > time:
                continue
            new = [str(i), 'DELETE', min_key]
            ans.append(new)
            del cache[min_key]
            curr_cache_size -= 1
        new = [str(i), 'PUT', id]
        ans.append(new)
        curr_cache_size += 1
        cache[id] = time
        min_key = min(cache, key=cache.get)
        min_value = cache[min_key]

for op in ans:
    print(' '.join(op))
