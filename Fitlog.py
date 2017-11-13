# export FLASK_APP=Fitlog.py  export FLASK_DEBUG=1／n flask run
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, url_for
from database import create_database, record_movement,record_fitdata,history_fitdata,Delect_fit,Delect_movement,export_fitdata
#from visual import dataVisual      #使用matlab生成
from visualbokeh import dataVisual  #使用bokeh生成

app = Flask(__name__)
app._static_folder = 'static'
# day_history = []

@app.route('/', methods=['GET','POST'])
def index():
    if request.form.get('history') == "历史数据":
        record = history_fitdata()
        return render_template('result.html',record = record)
    elif request.form.get('lastweek') == "一周Fit":
        dataVisual()
        return render_template('fitanalyze.html')

    return render_template('addExercise_form.html')


@app.route('/postmov', methods = ['POST'])
def get_post_mov_data():
    mdata = request.form['movdata']
    fitdate,fitdata = record_movement(mdata)
    record_fitdata(fitdate,fitdata) #将健身日期和本次动作存入健身数据库
    history_fitdata() #查看所有的健身数据
    return mdata

if __name__ == '__main__':
    app.run(debug=True)
