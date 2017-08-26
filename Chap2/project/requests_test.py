#! /usr/bin/env python
# -*- coding: utf-8 -*-


import requests

# r = requests.get('https://api.github.com/events') #<Response [200]>
# print(r)

# r = requests.post('http://httpbin.org/post',data = {'key':'value'} )
# print(r)

# r = requests.put('http://httpbin.org/put', data = {'key':'value'})
# print(r)
# r = requests.delete('http://httpbin.org/delete')
# print(r)
# r = requests.head('http://httpbin.org/get')
# print(r)
# r = requests.options('http://httpbin.org/get')
# print(r)

# #######

# #import requests
# r = requests.get('https://api.github.com/events')
# r.text
# r.content
# r.json()
# #u'[{"repository":{"open_issues":0,"url":"https://github.com/...



# try:

#     API = 'https://api.seniverse.com/v3/weather/now.json'
#     KEY = 'ozqwsdskrj99euhd'
#     location = input("请输入查询城市:")
#     LANGUAGE = 'zh-Hans'
#     UNIT = 'c'

#     query_needed_params = {'key' : KEY,
#                            'location' : location,
#                            'language' : LANGUAGE,
#                            'unit' : UNIT }
#     r = requests.get(API, params =query_needed_params, timeout =1)
#     if r.status_code = 200
#     print(r)
#     print('url:\n', r.url)
#     print('content:\n', r.text)
#     r = r.json()
#     weather = r.get('results')[0].get('now').get('text')
#     print('json:\n', r)
#     print(weather)

# except ReadTimeoutError as e:
#     print ("%s:网络超时,请您重新查询~")

# command = "city0"
# command_list = command.split(' ')

# if command_list[1] in ["0","1","2"]:
#     print (command_list)
# else:
#     print (",,,")
import sys
sys.path.append("..")
import weather_query_API as wqa


wqa.test()














