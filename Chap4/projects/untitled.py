#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
API Restructure
"""
__version__ = " v18.09.10.1106"
__author__ = 'NBR-hugh'
__license__ = 'MIT@2018-09'


########
# API
########

import requests

from const_value import API_NOW, KEY, LANGUAGE


import sqlite3


class SeniverseWeatherAPI():
    """The API of Seniverse Weather
    ref: https://www.seniverse.com/api
    params -> url -> request -> response -> JOSN
    """

    def __init__(self, city, unit):
        """Set SeniverseWeatherAPI request params."""
        self.key = KEY
        self.location = city
        self.url = API_NOW
        self.language = LANGUAGE
        self.unit = unit

        self.params = {}
        self.params_now = {
            'key': self.key,
            'location': self.location,
            'language': self.language,
            'unit': self.unit
        }
        # self.params_daily={}

    def get_response(self):
        print(">>> Begin now weather query...")
        response = requests.get(self.url, params=self.params_now, timeout=20)
        return response

    def judge_response(self):
        """Judge that if request weather info succeed
        response: a object
        api_info: a dict
            weather info dict:

            {'results':
                    [{'location': {'id': 'WT3Q0FW9ZJ3Q',
                                    'name': '武汉',
                                    'country': 'CN',
                                    'path': '武汉,武汉,湖北,中国',
                                    'timezone': 'Asia/Shanghai',
                                     'timezone_offset': '+08:00'},
                            'now': {'text': '多云',
                                    'code': '4',
                                    'temperature': '28'},
                    'last_update': '2018-09-11T11:25:00+08:00'}]}

            error dict:

            {'status': 'The location can not be found.',
            'status_code': 'AP010010'}
        """
        print(">>> Begin judge_response")
        response = self.get_response()

        if response.status_code == 200:
            print('>>> 心知天气 API 请求成功!')
            weather_info = response.json()
            api_info = weather_info

        else:
            print('>>> 心知天气 API 请求失败!')
            error_info = response.json()
            api_info = error_info

        return api_info

    def pick_weather_now(self, api_info):
        """Pick out now city weather.
        ref: https://www.seniverse.com/doc#now
        """
        print(">>>Begin pick_weather_now")

        print(">>>The API Return:", api_info)
        city = api_info['results'][0]['location']['name']
        date = api_info['results'][0]['last_update']
        weather_now = api_info['results'][0]['now']

        return date, city, weather_now


########
# 数据库
########


class WeatherDatabase():
    """docstring for WeatherDatabase"""

    def __init__(self, date, city, weather_now):
        self.date = date
        self.city = city
        self.weather_type = weather_now['text']
        self.temp = weather_now['temperature']
        self.code = weather_now['code']

        # 创建一个 table
        self.table_name = 'city_weather_now'
        self.create_table = '''
                            CREATE TABLE IF NOT EXISTS
                                city_weather_now(date date,
                                                city char,
                                                type char,
                                                temp char,
                                                code tinyint)
                            '''

        # 加入一行的天气信息
        self.row = (self.date, self.city,
                    self.weather_type, self.temp, self.code)
        self.insert_row = '''
                            INSERT INTO city_weather_now
                            VALUES(?,?,?,?,?)
                          '''

        # 根据城市获取天气信息
        self.select_rows = '''
                            SELECT date, city, type, temp , code
                            FROM city_weather_now
                            WHERE city = ? 
                            '''

    def single_operation_to_db(self, sql_commands, variable):
        """Execute a single  opeantion to database(SQLite): add,delete,update
        sql_comnads: a str,a single SQL statement(without ; )
        variable: a truple,table name/ clomuns name/ a insert raw..
        """
        print(">>>SQL 命令:", sql_commands)
        conn = sqlite3.connect('weather.db')
        c = conn.cursor()
        c.execute(sql_commands, variable)

        if 'SELECT' in sql_commands:
            select_result = c.fetchall()
            print(""">>>  IF 显示选取内容:""", select_result)
            return select_result

        conn.commit()
        conn.close()
        print('>>> 数据库单次操作成功!')

    def insert_a_row_weather(self):
        print(">>> 开始 insert 天气信息")
        sql_commands = self.insert_row
        variable = self.row
        self.single_operation_to_db(sql_commands, variable)
        print(">> insert ok !")

    def select_by_city(self, city):
        print(">>> 开始 select 天气信息")

        sql_commands = self.select_rows
        variable = (city,)
        print("选取城市:", city)
        select_result =  self.single_operation_to_db(sql_commands, variable)
        print(">> select ok !")

        return select_result


if __name__ == '__main__':
    api = SeniverseWeatherAPI("重庆", "unit")
    api_info = api.judge_response()
    print(api_info)
    date, city, weather_now = api.pick_weather_now(api_info)
    print(date, city, weather_now)

    db = WeatherDatabase(date, city, weather_now)
    db.insert_a_row_weather()
    select_result = db.select_by_city('重庆')
    print(">>> Select 返回结果:",select_result)