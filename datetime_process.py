#!/usr/env/bin python
import sys

for line in sys.stdin:
	line_ls = []
	line_ls.extend(line.strip().split(','))
	try:
		date, time, s = line_ls[0].split(' ')
	except ValueError:
		continue
	datetime = date+' '+time

	print '%s,%s,%s,%s,%s,%s,%s,%s,%s' % (datetime, line_ls[1], line_ls[2], line_ls[3], line_ls[4], line_ls[5], line_ls[6], line_ls[7], line_ls[8])