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
sys.path.append("/Users/NBR-hugh/Documents/github.nibirong.com/Py101-004/Chap1/project") # 让 python 解释器搜索该目录
import weather_query as wq
import requests

def get_API_requests(city,weather_dict,history_list):
    """
    发送 api 请求,对响应进行判断
    """
    API = 'https://api.seniverse.com/v3/weather/now.json'
    KEY = 'ozqwsdskrj99euhd'
    location = city
    LANGUAGE = 'zh-Hans'
    UNIT = 'c'

    query_needed = {'key' : KEY,
                    'location' : location,
                    'language' : LANGUAGE,
                    'unit' : UNIT }

    response = requests.get(API, params =query_needed, timeout =1) # 向 API 发送请求了

    if response.status_code == 200: #请求成功,打印相应天气信息并记录历史
        print("API 请求成功!")
        weather_dict,history_list = json_handle(response,weather_dict,history_list)

    elif response.status_code == 404: #未找到城市信息,用户重新输入
        print (response.status_code,
               '对不起,无该城市天气信息,请检查您的输入,或者查询其他城市...')
    else:
        print('抱歉,网络请求错误,请重试...')#其他错误代码,


def json_handle(response,weather_dict,history_list):
    """
    以 json 格式读取响应信息:城市 天气 温度
    """
    weather_json = response.json()  # 以 json 格式读取响应信息
    city = weather_json['results'][0]['location']['name']
    city_weather = weather_json['results'][0]['now']['text']
    city_temperature = weather_json['results'][0]['now']['temperature']
    iterm = f'{city} {city_weather} {city_temperature}摄氏度'
    print(iterm)

    weather_dict[city] = (city_weather,city_temperature)
    history_list.append(iterm)

    return weather_dict,history_list


def main():
    """
    主运行:提示信息,定义全局变量,进入互动的命令判读
    """
    print('# 天气API查询小程序')
    print('- 所有天气数据来自心知天气~')
    wq.help_info()

    # 设置变量,指令集
    weather_dict = {}
    history_list = []
    command_tuple = ('h', 'help','history','q','quit')

    while True:
        command = input("请输入查询城市:")

        try:
            if command in command_tuple:
                wq.command_work(command,history_list)
            else:
                get_API_requests(command,weather_dict,history_list)

        except EOFError:
            print('^D 强制退出...')
            exit(0)
        except KeyboardInterrupt:
            print('键盘打断,中断程序...')
            exit(0)
        except RuntimeError:
            print('请求超时,请确认网络状态,再重试...')


if __name__ == '__main__':
    main()
