# encoding: utf-8

import csv


with open('weather_info.csv',newline='') as cf:
    reader = csv.reader(cf)
    for row in reader:
        print(row)

# with open('weather_info.csv', newline='') as cf:
#     reader = csv.reader(cf, delimiter=':', quoting=csv.QUOTE_NONE)
#     for row in reader:
#         print(row)
