#!/usr/env/bin python
import sys

for line in sys.stdin:
	line = line.strip()
	try:
		date, time, s = line.split(',')[0].split()
		event_type = line.split(',')[1]
	except ValueError:
		continue
	

	print '%s,%s,%s' % (event_type, date, time)