
from flask import render_template, flash, redirect
from flask import Flask
from flask import request
from forms import FitForm
from database import create_database, record_movement,record_fitdata,history_fitdata,Delect_fit,Delect_movement,export_fitdata

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
def Weather_web():
    form = FitForm()
    #if form.validate_on_submit():
    if request.method == 'POST' and form.validate():
       if request.form['submit'] == "提交健身数据":
           mdata = [form.m1.data,form.m2.data,form.m3.data,form.m4.data,form.m5.data,form.m6.data,form.m7.data,form.m8.data,form.m9.data,form.m10.data]
           if form.fitdate.data !="": #判断日期是否提交，如果为空不能记录
               fitdata = record_movement(mdata) #记录本次运动的所有动作
               print(fitdata)
               print(form.fitdate.data)
               record_fitdata(form.fitdate.data,fitdata) #将健身日期和本次动作存入健身数据库
               error = 0
           else:
               error = 1

           return render_template('WeatherQuery.html',error = error,form=form)


       elif request.form['submit'] == "查看健身数据":
           record = history_fitdata() #查看所有的健身数据
           print (record)
           return render_template('WeatherIndex.html',form=form)

       elif request.form['submit'] == "清空健身数据库":
           Delect_fit()
           Delect_movement()
           return render_template('WeatherIndex.html',form=form)

    return render_template('WeatherIndex.html', 
                           form=form)



if __name__ == "__main__":
  app.run()