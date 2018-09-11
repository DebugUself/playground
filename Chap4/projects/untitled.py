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
        print("Begin now weather query...")
        response = requests.get(self.url, params=self.params_now, timeout=20)
        return response

    def judge_response(self):
        """Judge that if request weather info succeed
        response: a object
        api_info: a dict
        """
        response = self.get_response()

        if response.status_code == 200:
            print('心知天气 API 请求成功!')
            weather_info = response.json()
            api_info = weather_info

        else:
            print('心知天气 API 请求失败!')
            error_info = response.json()
            api_info = error_info

        return api_info

    def pick_weather_now(self, api_info):
        """Pick out now city weather.
        ref: https://www.seniverse.com/doc#now
        """
        print(api_info)
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
        #self.row = (date, city, weather_type, temp, code)
        #print (self.row)

        self.create_table = '''
                            CREATE TABLE IF NOT EXISTS
                                city_weather_now(date date,
                                                city char,
                                                type char,
                                                temp char,
                                                code tinyint)
                            '''
        self.insert_row = '''
                            INSERT INTO city_weather_now
                            VALUES(?,?,?.?,?)
                          '''

    def singl_operation(self):
        sql_commands = self.insert_row
        info = (self.date, self.city, self.weather_type, self.temp, self.code)
        print (info)
        print(sql_commands)
        conn = sqlite3.connect('weather.db')
        c = conn.cursor()
        c.execute( 'INSERT INTO city_weather_now VALUES(?,?,?,?,?)',('2018-09-11T10:05:00+08:00', '武汉', '多云', '27', '5'))
        conn.commit()
        conn.close()


if __name__ == '__main__':
    api = SeniverseWeatherAPI("武汉", "unit")
    api_info = api.judge_response()
    print(api_info)
    date, city, weather_now = api.pick_weather_now(api_info)
    print(date, city, weather_now)

    db = WeatherDatabase(date, city, weather_now)
    db.singl_operation()
