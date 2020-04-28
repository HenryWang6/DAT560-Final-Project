#!usr/env/bin python
import sys

flag_dic = {}
for line in sys.stdin:
	line = line.strip()
	event_type = line.split(',')[1]
	product_id = line.split(',')[2]
	user_id = line.split(',')[7]
	product_catgory = line.split(',')[4]

	if product_id =='' or product_id is None or user_id =='' or user_id is None:
		continue
	if product_catgory =='' or product_catgory is None:
		product_catgory = 'NULL'

	try:
		if event_type =='purchase':
			flag_dic[(product_id, user_id)][2] = True
		elif event_type =='cart':
			flag_dic[(product_id, user_id)][1] = True
		else:
			flag_dic[(product_id, user_id)][0] = True
	except ValueError:
		if event_type =='purchase':
			flag_dic[(product_id, user_id)] = [False, False, True]
		elif event_type =='cart':
			flag_dic[(product_id, user_id)] = [False, True, False]
		else:
			flag_dic[(product_id, user_id)] = [True, False, False]

	if sum(flag_dic[(product_id, user_id)]) != 3 and flag_dic[(product_id, user_id)][2]==True:
		print '%s,%s' % (product_id, product_catgory)