# -*- coding: utf-8 -*-

#读取csv并写入字典
import csv
csvFile = open('0601.csv', 'r')
reader = csv.reader(csvFile)
result = {}

for item in reader:
	if reader.line_num ==1:
		continue
	result[item[0]] = item[1]

csvFile.close()
print(result)

#查询字典
while True:
	x = input("請輸入查詢類別：")
	if x=='退出':
		break
	if x in result:
		print(result[x])