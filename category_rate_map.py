#!/usr/env/bin python

import sys
for line in sys.stdin:
	line = line.strip()
	category = line.split(',')[4]  # category code
	if category=='' or category is None:
		continue
	event_type = line.split(',')[1]
	if event_type =='' or event_type is None:
		continue

	print '%s,%s' % (category, event_type)