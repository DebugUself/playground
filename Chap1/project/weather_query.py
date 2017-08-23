#! /usr/bin/env python
# -*- coding: utf-8 -*-



import sys
from sys import exit
import csv

"""
Program name: weather_query
Author: NBR-hugh
Github: https://github.com/NBR-hugh/
Edition：v1.1
Edit date: 2017.08.20
"""

# abandon
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

#*Ding
# # 用户信息-历史记录存储
# def user(user_name,history_list):
#     user_history_dict[user_name] = history_list

# 根据城市查询对应天气,并添加查询记录
def weather_query(city,weather_dict,history_list):
    city_weather = weather_dict.get(city)
    record = city + ' ' + city_weather
    history_list.append(record)
    print(city,city_weather)

    return city_weather,history_list

# 退出程序,显示查询历史
def show_history (history_list):
    query_time = len(history_list)
    if query_time == 0:
        print('您还未查询,没有任何记录.')
    else:
        print('您的有效查询历史如下:')
        query_time = 0
        for i in history_list:
            query_time += 1
            print('第 %d 次查询:' % query_time,i)

#*   user(user_name,history_list)

def quit(history_list):
    show_history(history_list)
    print('''
          正在退出程序...
          感谢使用!
              ''')
    exit(0)


# 打印帮助信息
def help_info():
    print('''
    Tips:
    - 输入城市名，返回该城市最新的天气数据；
    - 输入h 或 help，获取帮助信息；
    - 输入history，获取历史查询信息；
    - 输入q 或 quit，退出程序的交互；
    ''')

def command_work(command,history_list):
    if command in ('h', 'help'):
        help_info()
    elif command in ('history'):
        show_history(history_list)
    elif command in ('q', 'quit'):
        quit(history_list)
    else:
        print("该指令不能操作")


def command_check(command,command_tuple,weather_dict,history_list):
    try:
        if command in command_tuple:
            command_work(command,history_list)
        elif weather_dict.get(command, None):
            city = command
            weather_query(city,weather_dict,history_list)
        else:
            print ("对不起,无该城市天气信息,请检查您的输入,或者查询其他城市!")

    except EOFError as e:
        print('^D 强制退出...')
        exit(0)
    except KeyboardInterrupt as e:
        print('键盘打断,中断程序...')
        exit(0)

# 主运行程序,根据用户输入判断执行的信息
def main():
    print('# 天气查询小程序')
    help_info()

    # 设置参数,变量
    weather_dict = {}
    history_list = []
    command_tuple = ('h', 'help','history','q','quit')
    filename = "weather_info.txt"
#*   user_name = input("您的用户名")
#*   user_history_dict = {}

    # 文件处理,得到天气字典
    weather_dict = csv_file_deal(filename,weather_dict)

    # 返回上次查询信息
    #print

    # 进入互动
    while True:
        command = input('>') # 接收用户信息

        command_check(command,command_tuple,weather_dict,history_list)




if __name__ == '__main__':
    main()
