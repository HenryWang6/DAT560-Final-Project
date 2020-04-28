#!/usr/env/bin python

import sys

dic = {}  # {(cate, brand): n%}
view_cnt = 0
purchase_cnt = 0

for line in sys.stdin:
	event_type, category, brand = line.strip().split(',')

	if event_type == 'view':
		view_cnt += 1
	elif event_type == 'purchase':
		purchase_cnt += 1
	else:

	try:
		dic[(category, brand)] = purchase_cnt *100.0 / view_cnt
	except ZeroDivisionError:
		if purchase_cnt>0:
			dic[(category, brand)] = 100.0
		else:
			dic[(category, brand)] = 0.0


print 'Category,Brand,Success Rate'
for key in dic.keys():
	print '%s,%s,%s' % (key[0],key[1],dic[key])