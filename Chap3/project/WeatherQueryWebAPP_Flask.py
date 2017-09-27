#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Program name: weather_query_API
Author: NBR-hugh
Github: https://github.com/NBR-hugh/
Edition：v1.0
Edit date: 2017.09.13
"""

from flask import Flask  #引入 flask 类
app = Flask(__name__)  #该类的一个示例就是WSGI交互程序

@app.route('/')  #告诉 flask 什么样的 url 可以触发函数
def hello_world() :  #函数名用于生成url,并返回想要呈现在用户浏览器的信息
    return "Hello,World!"


