~ 用于存放本周任务成果。

# CH1 天气查询程序说明

## Require

- Python 3.6.0

## Feature

- 输入中文城市名，返回该城市的天气数据;
- 输入指令 h or help，打印帮助文档;
- 输入指令 q or quit ，退出程序的交互;
- 输入指令 history, 打印查询历史.

## Usage

- 下载 [weather_query.py](https://github.com/NBR-hugh/Py101-004/blob/master/Chap1/project/weather_query.py)
- 在命令行中 cd 到 文件所在目录层级
- 在命令行中输入
   - python weather_query.py
- 跟随提示操作即可

## Explorer_Note&Record

- [WeatherInquiry_ExploringRecord.ipynb](https://github.com/NBR-hugh/Py101-004/blob/master/Chap1/note/CH1_WeatherInquiry_ExploringRecord.ipynb)

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

```java
--------- +
{END}     ^                                                                                   +-> exit {end}
          ^                                                                                   |
(print)   ^                                                                                   |-> "user quiry history"   +->"help info"
          ^                                                                                   |                          |
(out)     ^              +->weather_dict ----------+  +->city_weather,history_list --------+  +                          |
          ^              |                         |  |                                    |  |                          |
[function]^  main()   +->file_deal()               |  weather_query()                      |  quit()                     help()
          ^   |       |  |                         |  |                                    |  |                          |
(in)      ^   |       |  +<-filename,weather_dict  |  +<-weather_dict,city,history_list    |  +<- history_list           +
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
Waiting...|                                                                                (input)< ------------------------------------- +
--------- +
```

## Update

### v1.1

- [x] Bug:[重复查询的记录无法添加至历史记录](https://github.com/NBR-hugh/Py101-004/commit/ed73eb2a46d0066b7fb8fbea4058856d269f12c9##commitcomment-23712721)
    - 原因:数据类型的特点导致,字典中相同的 iterm 只会存储一次
    - 措施:将存放历史信息的数据类型由 dict 转变为 list
- [x] Pithy:阅读学友代码,发现判断形式更简短的表达方式
    - ` if commond == 'h' or commond == 'help':`
    - => `if commond in ['h','help']:`
    - `elif commond == 'q' or commond == 'quit':`
    - => `elif commond in ['q','quit']:`
- [?] Optimization:真正提升性能节省内存的代码
    - 触发: [Scotting](https://github.com/AIHackers/Py101-004/issues/42#issuecomment-322388219)
    - 探索记录:在[WeatherInquiry_ExploringRecord.ipynb](https://github.com/NBR-hugh/Py101-004/blob/master/Chap1/note/CH1_WeatherInquiry_ExploringRecord.ipynb)中更新
    - keypoint
       - 标准库 csv
            - [x] 定义,功能
            - [x] 示例代码解读
            - [x] 参数含义
            - [x] reader() 与 writer() 用法
            - [x] 与 file.read 的比较(参考@ Xiami)
        - collection
            - [x] 定义,功能
            - [x] 示例代码解读
            - [x] 主要用法
            - [?] 对读写的应用 -> 应该是 defaultdict 的 应用,后续再探
        - [扩展] python 性能判定
            - [ ] 程序性能有哪些判断指标?
            - [ ] 判断方法?
            - [ ] 优化方法?
- [ ] Optimization: @thxiami 的亮点&Review
    - 触发:[亮点](https://github.com/AIHackers/Py101-004/issues/64#issuecomment-323538602) | [code review](https://github.com/NBR-hugh/Py101-004/commit/455e936cee237a3f688cf6289a8d3179b27c46a7##commitcomment-23744561)
    - 探索记录:在[WeatherInquiry_ExploringRecord.ipynb](https://github.com/NBR-hugh/Py101-004/blob/master/Chap1/note/CH1_WeatherInquiry_ExploringRecord.ipynb)中更新
    - [x]  增加脚本开头的说明
    - [x]  给输入加一个异常判断呢？试着输入：windows：CTRL + Z / mac：Control + D
    - [x]  ` elif commond in weather_dict.keys():`
        - => `elif commond in weather_dict`
    - [x]  `elif commond in weather_dict.keys():`
        - => `elif weather_dict.get(commond, None)`
            - 更高效，使用键来找对应的key，而非遍历
    - [x]  修改 command
    - [ ]  利用字典调用函数
    - [ ]  class 封装用户信息

- [ ] Optimization:浏览评价 get 到的点
    - [x] [@ishanshan:调整readme结构, 用户与开发者分区](https://github.com/AIHackers/Py101-004/issues/47#issuecomment-323584531)
    - [ ] [探索使用__doc__](https://github.com/sea10253432/Py101-004/commit/f99df4119da6bae00bc4958a4897998f833e2ad4##commitcomment-23755835)
    - [ ] [优化文件目录固定](https://github.com/csyuxuan/Py101-004/commit/ce349f1ad62ef340452b7e18a8fcabfa2bbee005##commitcomment-23755486)
    - [ ]
    - [ ]

- [x] Reusable:改造让 CH2 让ch2可复用
    - [x] help()=>help_info(),防止与 python 内置函数冲突
    - [x] main()进行拆分
        - [x] error检查的command_check()
        - [x] 识别命令的 command_judge()
    - [x] 将 历史查询功能 history() 从 quit() 分离
    - [x] 在 if...else 中添加 history() 功能分支

