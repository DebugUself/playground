~ 用于存放本周任务成果。

# CH1 天气查询程序说明

## Require

- Python 3.6.0

## Feature

- 输入中文城市名，返回该城市的天气数据;
- 输入指令 h or help，打印帮助文档;
- 输入指令 q or quit ，退出程序的交互; 

## Steps

- 0.输入城市名，返回该城市的天气数据；
    - [x] 0.1 打开文件
        - with open("<filename>") as f:
    - [x] 0.2 读取文件内容
        - f.read()
        - f.readline()     
    - [x] 0.3 将文件内容转化成字典
        - str => list => dict
        - 0.3.1 将一行信息转化成字典
            - split()
            - d[k]= v
        - 0.3.2 将整个文本信息转化成字典
            - for line in weather_file:
    - [x] 0.4 查询互动与字典操作
            - input()
            - [(k,v)]= d.items()
            - v = d.get(k)
- [x] 1.帮助函数 help()
- [x] 2.退出函数 quit()
    - 2.1 输出的查询历史由字典换成文字
- [x] 3.主体判断与调试 main()


## Structure


            --------- +
            {END}     ^                                                                                   +-> exit {end}
                      ^                                                                                   |
            (print)   ^                                                                                   |-> "user quiry history"   +->"help info"
                      ^                                                                                   |                          |
            (out)     ^              +->weather_dict ----------+  +->city_weather,user_quiry_dict -----+  +                          |
                      ^              |                         |  |                                    |  |                          |
            [function]^  main()   +->file_deal()               |  weather_query()                      |  quit()                     help()
                      ^   |       |  |                         |  |                                    |  |                          |
            (in)      ^   |       |  +<-filename,weather_dict  |  +<-weather_dict,city,user_quiry_dict |  +<-(user_quiry_dict)       +
                      ^   |       |     ^        ^             |     ^            ^    ^               |  |   ^                      |
                      ^   |       |     |        |             +-----+            |    |               +--|---+                      |    
                      ^   |       |     |        |                                |    |                  |                          |
            (judge)   ^   |       |     |        |                              ?city  |              ?q or quit                ?h or help  ?wrong -> +
                      ^   |       |     |        |                                ^    |                  ^                          ^          ^     |
                      ^   |       |     |        |                                |    |                  |                          |          |     |
            {BEGIN}   ^   +-----> + --> + -----> + -----------------------------> + -- + -----------------+------------------------> + -------- +     |
            --------- +                                                           ^                       ^                          ^                |
                      ^                                                           |                       |                          |                |
                      |                                                           + ----- ------------- commond -------------------- +                |
                      |                                                                                   |                                           |
                      |                                                                                   +                                           |
            Waiting...|                                                                                (input)<-------------------------------------- +
            --------- +


## Using

- 下载 [weather_query.py](https://github.com/NBR-hugh/Py101-004/blob/master/Chap1/project/weather_query.py)
- 在命令行中 cd 到 文件所在目录层级
- 在命令行中输入
   - python weather_query.py
- 跟随提示操作即可

## Note&Record

- [WeatherInquiry_ExploringRecord.ipynb](https://github.com/NBR-hugh/Py101-004/blob/master/Chap1/project/CH1_WeatherInquiry_ExploringRecord.ipynb)
