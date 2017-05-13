#filename:8csv_readline_pop
# -*- coding: utf-8 -*-

file = open('0601.csv', 'r')
data = {}
for line in file.readlines():
	line = line.strip('\n')
	line = line.split(',')
	key = line.pop(0)
	value = line.pop(0)
	data[key] = value

print(data)

file.close()