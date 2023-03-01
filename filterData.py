data = [
		{'city': 'indore', 'population': '5000000', 'state': 'Mp', 'code': 452001},
		{'city': 'Bhopal', 'population': '6000000', 'state': 'Mp', 'code': 452011},
		{'city': 'chennai', 'population': '10000000', 'state': 'TN', 'code': 552001},
		{'city': 'chennai', 'population': '9000000', 'state': 'TN', 'code': 562001},
		{'city': 'banglore', 'population': '5500000', 'state': 'Kn', 'code': 452111},
		{'city': 'indore', 'population': '7000000', 'state': 'Mp', 'code': 452010},
		{'city': 'Jaipur', 'population': '9900000', 'state': 'Rj', 'code': 442001},
		{'city': 'indore', 'population': '4500000', 'state': 'Mp', 'code': 452000},
		{'city': 'Bhopal', 'population': '6540000', 'state': 'Mp', 'code': 452211},
		{'city': 'Bhopal', 'population': '2000000', 'state': 'Mp', 'code': 462011},
		{'city': 'Jaipur', 'population': '9800000', 'state': 'Rj', 'code': 442201},
		{'city': 'Jaipur', 'population': '9700000', 'state': 'Rj', 'code': 422001},
		{'city': 'banglore', 'population': '5600000', 'state': 'Kn', 'code': 402111},
		{'city': 'manglore', 'population': '5550000', 'state': 'Kn', 'code': 442111},
		]

formatedData = {}
sorted_data = sorted(data, key = lambda i: int(i['population']), reverse=True)


for i in sorted_data:
	if i['city'] not in formatedData:
		formatedData[i['city']] = [{i['population']: i['code']}]
	else:
		if len(formatedData[i['city']]) <2:
			formatedData[i['city']].append({i['population']: i['code']})

print(formatedData)

for k,v in formatedData.items():
	print('{} top populated cities code is......'.format(k))
	for j in v:
		print(list(j.values())[0])
