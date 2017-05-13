#filename:python3 name_check.py
# -*- coding: utf-8 -*-

file = open('name.csv', 'r')

for line in file.readlines():
	line = line.strip('\n')
	line = line.split(',')	
	iterm = line.pop(-1)
	if iterm == 'py':
		py_iterm = line.pop(1)
		print("您本周书写的py脚本是：%s" % py_iterm)
	
file.close()