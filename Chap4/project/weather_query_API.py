#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Program name: weather_query_API
Author: NBR-hugh
Github: https://github.com/NBR-hugh/
Edition：v1.0
Edit date: 2017.08.23
"""

import requests

import API_deal
import utils.command_func as command_func


def main():
    """
    主运行:提示信息, 定义全局变量, 进入互动的命令判读
    """
    print('# 天气API查询小程序')
    print('- 所有天气数据来自心知天气~')
    print(command_func.help_info("NOW"))

    # 设置变量, 指令集
    history_list = []
    command_tuple = ('h', 'help', 'history', 'q', 'quit')
    unit_switch_tuple = ('c', 'f')
    API_tuple = ('owm')
    unit = "c"

    while True:
        command = input(">>> 请输入指令或查询城市:")
        command_list = command.split(' ')

        try:
            if command in command_tuple:
                command_func.command_work(command, history_list)
            elif command in unit_switch_tuple:
                unit = command
                print("转换成功")
            elif command in ('d'):
                daily_mode(unit, history_list)
            elif command in ('owm'):
                switch_owm_api(unit, history_list)
            else:
                API_deal.get_API_now(unit, command_list[0], history_list)

        except EOFError:
            print('^D 强制退出...')
            exit(0)
        except KeyboardInterrupt:
            print('键盘打断, 中断程序...')
            exit(0)
        except IndexError:
            print('NOW_MODE:命令错误, 请根据提示检查格式, 重新查询')
            print(command_func.help_info("NOW"))
        except requests.exceptions.Timeout:
            print('请求超时, 请确认网络状态, 再重试...')


def daily_mode(unit, history_list):
    """
    DailyMode: 识别 城市,数字, 与指令 q, 捕捉错误
    """
    command_func.help_info("DAILY")

    while True:
        command = input(""">>>DAILY MODE|请输入城市与日期信息:""")
        command_list = command.split(" ")

        try:
            if command == "q":
                print("退出DAILY MODE...成功!")
                break
            else:
                API_deal.get_API_daily(unit, command_list, history_list)
        except IndexError:
            print('Daily_MODE:命令错误, 请根据提示检查格式, 重新查询')


def switch_owm_api(unit, history_list):
    command_func.help_info("OWM")

    while True:
        command = input(""">>>OWM API|Please input city name:""")

        try:
            if command == "q":
                print("退出DAILY MODE...成功!")
                break
            else:
                API_deal.get_owm_weather_now(unit, command, history_list)
        except IndexError:
            print('Daily_MODE:命令错误, 请根据提示检查格式, 重新查询')


if __name__ == '__main__':
    # get_API_daily()
    main()
