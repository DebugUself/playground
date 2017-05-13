#filename:python3 11pop_sum_dict.py
# -*- coding: utf-8 -*-

file = open('0601a.csv', 'r')
data1 = []
data2 = []
sum0 = 0
for line in file.readlines():
	line = line.strip('\n')
	line = line.split(',')
	iterm1 = line.pop(0)
	iterm2 = line.pop(0)
	iterm2_float = float(iterm2)
	sum0 = sum0 + iterm2_float
	print(sum0)

print(sum0)

housework_dic = {}
housework_dic[iterm1] = sum0
print(housework_dic)
	
file.close()