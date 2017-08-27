#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Program name: weather_query_API
Author: NBR-hugh
Github: https://github.com/NBR-hugh/
Edition：v1.0
Edit date: 2017.08.23
"""

import sys
sys.path.append("..")
import API_deal as ad

def unit_switch(command):
    unit = command

    return unit




def command_work(command,weather_dict,history_list):
    if command in ('h', 'help'):
        help_info("NOW")
    elif command in ('history'):
        show_history(history_list)
    elif command in ('q', 'quit'):
        quit(history_list)
    else:
        print("该指令不能操作")

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
def help_info(help_type):
    help_dict={
    "NOW" : """
        Tips:
        - 输入城市名称,获取即时天气信息
        - 输入h 或 help，获取帮助信息；
        - 输入history，获取历史查询信息；
        - 输入q 或 quit，退出程序的交互；
        - 输入c, 显示摄氏度单位
        - 输入f. 显示华氏度单位
        - 输入d,进入日期查询模式
        """,

    "DAILY" : """
        DAILY MODE:
        - 欢迎进入日期查询模式!
        - 输入"城市 数字",获取今起三天的天气预报,如:
            - "武汉 0"  获取武汉今日天气信息
            - "武汉 1"  获取武汉明日天气预报
            - "武汉 2"  获取武汉后日天气预报
        - 输入 q 退出该模式
        """
    }

    print(help_dict[help_type])




