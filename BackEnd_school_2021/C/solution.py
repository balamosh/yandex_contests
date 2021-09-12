import sys, datetime

t, e = map(int, input().split())

critical_date = datetime.datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0)
last_dates = [critical_date]
date_to_errors = {critical_date: 0}
errors = 0
critical_moment = False

for line in sys.stdin:
    if critical_moment:
        continue
    line = line.split()
    date_str = line[0][1:]
    time_str = line[1][:-1]
    status = line[2]
    curr_year, curr_month, curr_day = map(int, date_str.split('-'))
    curr_hour, curr_minute, curr_second = map(int, time_str.split(':'))
    date = datetime.datetime(year=curr_year, month=curr_month, day=curr_day, hour=curr_hour, minute=curr_minute, second=curr_second)
    if date not in date_to_errors:
        date_to_errors[date] = 0
    if status == 'ERROR':
        date_to_errors[date] += 1
        errors += 1
    if date != last_dates[-1]:
        last_dates.append(date)
    while last_dates:
        diff = date - last_dates[0]
        if diff.total_seconds() < t:
            break
        errors -= date_to_errors[last_dates[0]]
        del date_to_errors[last_dates[0]]
        last_dates.pop(0)
    if errors >= e:
        critical_date = date
        critical_moment = True

if not critical_moment:
    print(-1)
else:
    print(critical_date)
