#!usr/env/bin python
import sys

category_view = {}
category_cart = {}
category_purchase = {}

for line in sys.stdin:
	category, event_type= line.strip().split(',')

	if event_type == 'view':
		try:
			category_view[category] +=1
		except ValueError:
			category_view[category] = 1
		
	if event_type =='cart':
		try:
			category_cart[category] += 1
		except ValueError:
			category_cart[category] = 1

	if event_type =='purchase':
		try:
			category_purchase[category] += 1
		except ValueError:
			category_purchase = 1


print 'category\t\tview_to_cart_rate\t\tcart_to_purchase_rate\t\tpurchase_rate'
for key in category_view_cart.keys():
	print '%s\t%s\t%s\t%s' % (key, category_cart[key]*100.0/category_view[key], category_purchase[key]*100.0/category_cart[key], category_purchase[key]*100.0/category_view[key])