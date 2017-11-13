#coding = 'utf-8'
import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
from bokeh.charts import Bar, output_file, show
from bokeh.io import export_png
from bokeh.sampledata.autompg import autompg as df


def dataVisual():
    #打开文件
    df = pd.read_csv('raw.csv/2FITMOVEMENT-Table 1.csv')
    #列出运动
    UniqueAct = df.exercise.unique()
    #选出深蹲
    sl = df[df['exercise'].isin(['深蹲'])]
    #添加每条重量加乘
    sl['weights'] = sl.apply(lambda x: x.repetition*x.set*x.weight, axis=1)
    #列出日期
    Uniquedate = df.date.unique()
    
    #日期和重量累积的矩阵
    date = []
    ws = []
    
    for i in Uniquedate:
        date.append(i)
        ws.append(np.sum(sl[sl['date'].isin([i])])['weights'])
        d = {'date': date,
                 'weights':ws}
    st = pd.DataFrame(d)
    p = Bar(st,  'date', values='weights', title="深蹲累积" )
    # add a line renderer with legend and line thickness
    #output_file("bar.html")
    #show(p)

    export_png(p,filename="static/output.png")

    #plt.savefig("output.png")
    #p = st.plot.bar(x='date',y='weights',title="FitAnalyze")
    #fig = p.get_figure()
    #fig.savefig("static/output.jpg")
    #p.figure.savefig("static/output.jpg")

if __name__ == '__main__':
   dataVisual()
