# CH2  API 天气查询 程序说明

## Require

- python 3.6
- requests 2.14.2

## Feature

- 输入中文城市名，返回该城市最新的天气数据;
- 输入指令 h or help，打印帮助文档;
- 输入指令 q or quit ，退出程序的交互;
- 输入指令 history, 打印查询历史.

## Usage

- 下载`util`, `weather_query.py` 与 `weather_query_API.py` 至同一目录层级
- 在命令行中 cd 到 文件所在目录层级
- 在命令行中输入 `python weather_query_API.py`
- 跟随界面提示信息操作即可

## Explorer_Note&Record

- [CH2\_WeatherInquiryAPI\_ExploringRecord.ipynb](https://github.com/NBR-hugh/Py101-004/blob/master/Chap2/note/CH2_WeatherInquiryAPI_ExploringRecord.ipynb)

## Steps

- 00 In 城市名 Out 最新的天气数据
    - 00.1 调用文件获取天气信息 => 调用 API 获取天气信息
        - 0 什么是 api?
            - 服务员
        - 1 选择 api
            - 心知
            - OWM
        - 2 如何调用 api?
            - requests.get(url,param,timeout)
        - 3 JOSN 信息如何处理
            - requests.get.JOSN()
            - 观察:返回的字典与数列组合格式,逐层提取
                - `weather = r.['results'][0]['now']['text']`
        - 4 对请求的不同响应进行判断
            - requests.status_code()

- 01 help(),history(),quit(),main()
    - 01.0 不同目录层级的 imports
        - 01.0.1 方便用户的引入路径
            - 放置于同一文件夹
    - 01.1 改造 ch1 的 weathr_query.py, 使其能够复用
    - 01.2 调通主程序main()

## Structure


```java
--------- +
{END}     ^                                                               + ->exit()
          ^                                                               |
(print)   ^                + ->"help_info"  + ->"history" & "help_info"   |               + ->"c error"    + -> "city,weather,temp"            + -> 'NOT FOND'
          ^                |                |                             |               |                |                                   |
[out]     ^                |                |                             |               |                +-> weather_dict,history_list       +-------> + ---> +
          ^                |                |                             |               |                |                                   |         ^      |
[function]^                +-wq.help_info() +-wq.show_history()           +-wq.quit()     |                +-json_handle()                     |         |      |
          ^                |                |                             |               |                |                                   |         |      |
[in]      ^                |                history_list                  +history_list   |                +response,weather_dict,history_list |         |      |
          ^                |                |         ^                   |         ^     |                |                   ^         ^     |         |      |
(judge)   ^                ?h,help          ?history  |                   ?quit     |     ?else            ?200                |         |     ?404      ?else  |
          ^                ^                ^         |                   ^         |     ^                ^                   |         |     ^         ^      |
          ^                |                |         |                   |         |     |                |                   |         |     |         |      |
          ^                + -------------- + --------------------------- + ------------- +                + --------------------------------- + ------- +      |
          ^                |                          |                             |                      |                   |         |                      |
[pass]    ^             command     history_list----- + --------------------------- +             response.status_code         |         |                      |
          ^                ^        ^                                                                      ^                   |         |                      |
          ^                +--------+                                                                      |                   |         |                      |
          ^                |                                                                               |                   |         |                      |
[function]^  +main()       +wq.command_work()                                                              +get_API_requests() |         |                      |
          ^  |             |                                                                               |                   |         |                      |
[in]      ^  |             +-command                                                                       +city,    weather_dict,history_list                  |
          ^  |                 ^                                                                           ^              ^        ^                            |
          ^  |                 |                                                                           |              |        |                            |
(judge)   ^  |             ?command:in command_tuple                                                       ?command:else  |        |                            |
          ^  |             ^                                                                               |              |        |                            |
          ^  |             |                                                                               |              |        |                            |
{BEGIN}   ^  + ----------> + ----------------------------------------------------------------------------- + ------------ + ------ +                            |
--------- +                ^                                                                                                                                    |
          |             command                                                                                                                                 |
          |                |                                                                                                                                    |
waiting...|              (input) <----------------------------------------------------------------------------------------------------------------------------- +
--------- +
```

## Update

- [x] 温度单位转换
- [x] 将API的请求的变量分离出来成为变量配置文件
    - => [Wangjunyu: 模仿心知天气demo的模块化尝试](https://github.com/Hugo1030/Py101-004/commit/e39f2cf738e527b5dbef1dbc3d2d8ec0f93859bf##commitcomment-23845207)
    - [=> demo](https://github.com/seniverse/seniverse-api-demos/blob/master/python/utils/const_value.py)
- [ ] 指定日期查询代码
- [ ] 查询外国 API :OWM
- [ ] 




