#!usr/env/bin python
import sys

category_view = {}
category_cart = {}
category_purchase = {}
category_ls = []

for line in sys.stdin:
	category, event_type= line.strip().split(',')

	if event_type == 'view':
		try:
			category_view[category] +=1
		except KeyError:
			category_view[category] = 1
		category_ls.append(category)
		
	if event_type =='cart':
		try:
			category_cart[category] += 1
		except KeyError:
			category_cart[category] = 1
		category_ls.append(category)

	if event_type =='purchase':
		try:
			category_purchase[category] += 1
		except KeyError:
			category_purchase[category] = 1
		category_ls.append(category)

category_set = set(category_ls)

print 'category,view_to_cart_rate,cart_to_purchase_rate,view_to_purchase_rate'
for each in category_set:
	try:
		v_to_c = category_cart[each]*100.0/category_view[each]
	except KeyError:
		v_to_c = 0.0

	try:
		num_vp = category_view[each]-category_cart[each]
		v_to_p = num_vp*100.0/category_view[each]
	except KeyError:
		num_vp = 0
		v_to_p = 0.0

	try:
		num_cp = category_purchase[each] - num_vp
		c_to_p = category_purchase[each]*100.0/category_cart[each]
	except KeyError:
		c_to_p = 0.0

	print '%s,%s,%s,%s' % (each, v_to_c, c_to_p, v_to_p)


