#!/usr/env/bin python

import sys

for line in sys.stdin:
	line = line.strip()

	event_type = line.split(',')[1]  # event type
	category = line.split(',')[4]
	brand = line.split(',')[5]  # brand

	if (event_type=='' or event_type is None) or (category=='' or category is None) or (brand=='' or brand is None):
		continue
	
	print '%s\t%s\t%s' % (event_type, category, brand)