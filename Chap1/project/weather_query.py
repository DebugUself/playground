#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from sys import exit
import csv
# 打开文件,将文件内容转化成字典(dict)
# def file_deal(filename,weather_dict):
#     with open(filename) as weather_file:
#         for line in weather_file:
#             file_list = line.split(",")
#             weather_dict[file_list[0]] = file_list[1]

#     return weather_dict

# v1.1 文件打开用csv优化,提升运行速度
def csv_file_deal(filename,weather_dict):
    with open(filename,newline = '') as weather_file:
        reader = csv.reader(weather_file)
        for k,v in reader:
            weather_dict[k] = v
    return weather_dict

# 根据城市查询对应天气,并添加查询记录
def weather_query(city,weather_dict,history_list):
    city_weather = weather_dict.get(city)
    record = city + ' ' + city_weather
    history_list.append(record)
    print(city,city_weather)

    return city_weather,history_list

# 退出程序,显示查询历史
def quit (history_list):
    query_times = 0
    print('您的查询历史如下:')
    for i in history_list:
        query_times += 1
        print('第 %d 次查询:' % query_times,i)

    print('''
    正在退出程序...
    感谢使用!
    ''')
    exit(0)

# 打印帮助信息
def help():
    print('''
    - 输入城市名，返回该城市的天气数据;
    - 输入指令 h or help，打印帮助文档;
    - 输入指令 q or quit ，退出程序的交互;
    ''')
# 主运行程序,根据用户输入判断执行的信息
def main():
    print('''
     # 天气查询小程序

     TIPS:

    - 输入中文城市名，返回该城市的天气数据;
    - 输入指令 h or help，打印帮助文档;
    - 输入指令 q or quit ，退出程序的交互;
    ''')

    # 设置参数,变量
    weather_dict = {}
    history_list = []
    filename = "weather_info.txt"

    # 文件处理,得到天气字典
    weather_dict = csv_file_deal(filename,weather_dict)

    # 进入互动
    while True:
        #weather_dict = weather_dict
        commond = input('>') # 接收用户信息

        if commond == 'h' or commond == 'help':
            help()
        elif commond == 'q' or commond == 'quit':
            quit(history_list)
        elif commond in weather_dict.keys():
            city = commond
            weather_query(city,weather_dict,history_list)
        else:
            print ("对不起,无该城市天气信息,请检查您的输入,或者查询其他城市!")


if __name__ == '__main__':
    main()
