#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Program name: weather_query_API
Author: NBR-hugh
Github: https://github.com/NBR-hugh/
Edition: v1.0
Edit date: 2017.09.13
"""

from flask import Flask # 引入 flask 类
from flask import render_template # 引入渲染模板
from flask import request
from .API_deal import get_API_now

app = Flask(__name__)  #该类的一个示例就是WSGI交互程序

class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg



@app.route('/',methods=["POST","GET"])  #告诉 flask 什么样的 url 可以触发函数
def index_func(DisplayInfo=None) :  #函数名用于生成url,并返回想要呈现在用户浏览器的信息
    unit = "c"
    DisplayInfo="欢迎使用~"

    # 功能1:帮助
    if 'help' in request.form.keys():
        help_info=help_func()
        display_info=help_info

    # 功能2:查询
    elif 'query' in request.form.keys():
        city =request.form['input_text']
        API_return =get_API_now(unit, city)
        weather_info =API_return[0]
        print(history_list)
        display_info =weather_info

    elif 'history' in request.form.keys():
        history_info =history_list
        display_info =history_info

    else:
        display_info= "Have A Good Day! :D"

    history_list.append(weather_info)
    return render_template('Index.html',DisplayInfo=display_info)

def help_func():
    help_info= """
    帮助信息:
        - 输入要查询的城市名称,回车确认将返回即时天气信息;
        - 点击"help"按钮,显示帮助信息;
        - 点击" history"按钮,显示查询历史. 
               """
    return help_info


if __name__ == '__main__':
    app.run(debug=True)


