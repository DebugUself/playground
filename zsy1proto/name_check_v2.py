#filename:python3 name_check.py
# -*- coding: utf-8 -*-

def openfile():
	file = open('name.csv', 'r')
	print(file)

def getName(file):
	for line in file.readlines():
		line = line.strip('\n')
		line = line.split(',')	
		iterm = line.pop(-1)
		print(iterm)


	if iterm == 'py':
		py_iterm = line.pop(1)
		print("您本周书写的py脚本是：%s" % py_iterm)
	
file.close()

openfile()
getName()