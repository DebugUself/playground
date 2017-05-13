# filename:7csv_dictreader.py
# -*- coding: utf-8 -*-

import csv
f = open('0601.csv', 'r')
for row in csv.DictReader(f):
	print(row['活动类别'])
f.close()