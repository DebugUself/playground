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
from API_deal import get_API_now

app = Flask(__name__)  #该类的一个示例就是WSGI交互程序

@app.route('/',methods=["POST","GET"])  #告诉 flask 什么样的 url 可以触发函数
def index_func(DisplayInfo=None) :  #函数名用于生成url,并返回想要呈现在用户浏览器的信息
    unit = "c"

    # 功能1:帮助
    if 'help' in request.form.keys():
        help_info =help_func()

        return render_template('Index.html',DisplayInfo=help_info)

    # 功能2:查询
    elif 'input_text' in request.form.keys():
        city =request.form['input_text']
        API_return =get_API_now(unit, city)
        weather_info =API_return

        return render_template('Index.html',DisplayInfo=weather_info)

    # 功能3:历史
    elif 'history' in request.form.keys():
        with open('QueryHistory.txt') as query_history:
            history_info =query_history.read()

        return render_template('Index.html',DisplayInfo=history_info)

    else:
        welcome_info ="Have A Good Day! please enjoy~ :D"

        return render_template('Index.html',DisplayInfo=welcome_info)




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


