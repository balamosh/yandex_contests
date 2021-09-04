def parse_phone_number(in_str):
	number_str = ''.join(c for c in in_str if c.isdigit())
	if len(number_str) == 7:
		return 495, int(number_str)
	elif len(number_str) == 11:
		return int(number_str[1:4]), int(number_str[4:11])

add_number = parse_phone_number(input())
for i in range(3):
	check_number = parse_phone_number(input())
	if add_number == check_number:
		print("YES")
	else:
		print("NO")
