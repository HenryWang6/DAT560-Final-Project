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
		except ValueError:
			category_cart[category] = 1
		category_ls.append(category)

	if event_type =='purchase':
		try:
			category_purchase[category] += 1
		except ValueError:
			category_purchase = 1
		category_ls.append(category)


print 'category,view_to_cart_rate,cart_to_purchase_rate,purchase_rate'
for each in category_ls:
	print '%s,%s,%s,%s' % (each, category_cart[each]*100.0/category_view[each], category_purchase[each]*100.0/category_cart[each], category_purchase[each]*100.0/category_view[each])