numbers = input().split(' ')
t_room = int(numbers[0])
t_cond = int(numbers[1])
mode = input()

t_new = t_room

if mode == "freeze":
    if t_room > t_cond:
        t_new = t_cond
elif mode == "heat":
    if t_room < t_cond:
        t_new = t_cond
elif mode == "auto":
    t_new = t_cond

print(t_new)
