#!usr/env/bin python
import sys

id_cnt = {}
id_cat_dic = {}
for line in sys.stdin:
	product_id, category = line.strip().split(',')

	id_cat_dic[product_id] = category

	try:
		id_cnt[product_id] += 1
	except KeyError:
		id_cnt[product_id] = 1

print 'product_id,inhesitate_purchase_count,category'
for key in id_cnt.keys():
	print '%s,%s,%s' % (key, id_cnt[key], id_cat_dic[key])

