#!/usr/env/bin python

'''Mapper: calculated which category has the highest rate'''
import sys
for line in sys.stdin:
	line = line.strip()
	category = line.split(',')[4]  # category code
	if category=='' or category is None:
		continue
	event_type = line.split(',')[1]
	if event_type =='' or event_type is None:
		continue

	print '%s\t%s' % (category, event_type)