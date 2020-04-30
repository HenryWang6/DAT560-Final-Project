#!/usr/env/bin python
import sys

ls = []
for line in sys.stdin:
	event_type, date, time = line.strip().split(',')
	ls.append((event_type,date,time))

print 'event_type,date,time'
for each in ls:
	print '%s,%s,%s' % (each[0], each[1], each[2])
