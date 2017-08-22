import sys
sys.path.insert(0,
    "/Users/NBR-hugh/Documents/github.nibirong.com/Py101-004/Chap1/project") # 让 python 解释器搜索该目录
import weather_query as wq
import request

def API_request():

    # 定义参数
    API = 'https://api.seniverse.com/v3/weather/now.json'
    KEY = 'ozqwsdskrj99euhd'
    location = input("请输入查询城市:")
    LANGUAGE = 'zh-Hans'
    UNIT = 'c'
    query_needed = {'key' : KEY,
                    'location' : location,
                    'language' : LANGUAGE,
                    'unit' : UNIT }

    # requests,josn 处理
    weather_response = requests.get(API, params =query_needed, timeout =1) # 向 API 发送请求
    r = r.json()  # 以 json 格式读取响应信息
    weather = r.get('results')[0].get('now').get('text')    # 根据信息内容提取天气信息

    return weather_dict

def main():
    print('# 天气API查询小程序')

    wq.help()
    # 设置参数,变量
    weather_dict = {}
    history_list = []

    weather_dict = API_request()
    user_interaction(weather_dict,history_list)


if __name__ == '__main__':
    main()
