#filename:python3 12housework_dict_inquiry.py
# -*- coding: utf-8 -*-

# 计算家务持续总时间
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

# 把家务和家务持续时间进行配对
housework_dic = {}
housework_dic[iterm1] = sum0

# 查询家务时间
while True:
	x = input("請輸入查詢類別：")
	if x=='退出':
		break
	if x=='家务':
		print(housework_dic[x])

# 谢幕	
file.close()