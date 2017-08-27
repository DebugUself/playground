#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Program name: weather_query_API
Author: NBR-hugh
Github: https://github.com/NBR-hugh/
Edition：v1.0
Edit date: 2017.08.23
"""
import utils.command_func as cf
import API_deal as ad
import requests



def main():
    """
    主运行:提示信息,定义全局变量,进入互动的命令判读
    """
    print('# 天气API查询小程序')
    print('- 所有天气数据来自心知天气~')
    print (cf.help_info("NOW"))


    # 设置变量,指令集
    weather_dict = {}    #整个文件读取天气时起作用
    history_list = []
    command_tuple = ('h', 'help','history','q','quit')
    unit_switch_tuple = ('c','f')
    unit = "c"

    while True:
        command = input(">>> 请输入指令或查询城市:")
        command_list = command.split(' ')

        try:
            if command in command_tuple:
                cf.command_work(command,weather_dict,history_list)
            elif command in unit_switch_tuple:
                unit = command
                print("转换成功")
            elif command in ('d'):
                daily_mode(unit,weather_dict,history_list)
            else:
                ad.get_API_now(unit,command_list[0],weather_dict,history_list)

        except EOFError:
            print('^D 强制退出...')
            exit(0)
        except KeyboardInterrupt:
            print('键盘打断,中断程序...')
            exit(0)
        except IndexError:
            print('NOW_MODE:命令错误,请根据提示检查格式,重新查询')
            print (cf.help_info("NOW"))
        except requests.exceptions.Timeout:
            print('请求超时,请确认网络状态,再重试...')

def daily_mode(unit,weather_dict,history_list):
    cf.help_info("DAILY")

    while True:
        command = input(""">>>DAILY MODE|请输入城市与日期信息:""")
        command_list = command.split(" ")
        print (command_list)

        try:
            if command == "q":
                print("退出DAILY MODE...成功!")
                break
            else:
                result = ad.get_API_daily(unit,command_list,weather_dict,history_list)
                print (result)
        except IndexError:
            print('Daily_MODE:命令错误,请根据提示检查格式,重新查询')


if __name__ == '__main__':
    #get_API_daily()
    main()
