import requests
from utils.const_value import API_NOW, KEY, LANGUAGE,\
                              API_DAILY, START, DAYS


def test():
    print("ok!")

def get_API_now(unit,city,weather_dict,history_list):
    """
    发送 now_api 请求,对响应进行判断处理, 显示天气,添加至历史记录
    """
    print ("get_API NOW begin!")
    weather_josn = get_response(unit,city,API_NOW)
    if weather_josn != None:
        iterm = josn_now_deal(unit,weather_josn)
        history_list.append(iterm)

def get_API_daily(unit,city_num_list,weather_dict,history_list):
    """
    发送 daily_api 请求,对响应进行判断处理, 显示天气,添加至历史记录
    """
    city = city_num_list[0]
    day_num = city_num_list[1]

    print ("get_API_daily begin!")
    weather_josn = get_response(unit,city,API_DAILY)
    if type(weather_josn) != None:
        iterm = josn_daily_deal(unit,weather_josn,day_num)
        history_list.append(iterm)
    else:
        print("please check weather_josn")

def get_response(unit,city,API):
    """
    发送API请求,对响应进行判断
    """
    query_needed = {'key' : KEY,
                    'location' : city,
                    'language' : LANGUAGE,
                    'unit' : unit}

    response = requests.get(API, params =query_needed, timeout =20) # 向 API 发送请求了

    if response.status_code == 200: #请求成功,打印相应天气信息并记录历史
        print("API 请求成功!")
        return response.json()
    elif response.status_code == 404: #未找到城市信息,用户重新输入
        print (response.status_code,
               '对不起,无该城市天气信息,请检查您的输入,或者查询其他城市...')
    else:
        print('抱歉,网络请求错误,请重试...') #其他错误代码


def josn_now_deal(unit,weather_josn):
    """
    将 nowAPI 响应转化成用户所见信息
    """
    # 提取 API 信息
    city = weather_josn['results'][0]['location']['name']
    city_weather = weather_josn['results'][0]['now']['text']
    city_temp_c = weather_josn['results'][0]['now']['temperature']
    update_time = weather_josn['results'][0]['last_update']

    # 提取 单位信息
    unit_dict = unit_change(unit)
    temp_unit = unit_dict["temp_unit"]

    # 显示用户可见信息
    iterm = f"""
             城市:{city}
             天气:{city_weather}
             温度:{city_temp_c} {temp_unit}
             """
    print(iterm)

    return iterm

def josn_daily_deal(unit,weather_josn,day_num):
    """
    对 dailyAPI 响应转化成用户所见信息
    """
    # 提取 API 信息
    city = weather_josn['results'][0]['location']['name']
    day = weather_josn['results'][0]['daily'][int(day_num)]
    date = day['date']
    text_day = day['text_day']
    text_night = day['text_night']
    high_temp = day['high']
    low_temp = day['low']
    wind_direction = day['wind_direction']
    wind_speed = day['wind_speed']

    # 提取 单位信息
    unit_dict = unit_change(unit)
    temp_unit = unit_dict["temp_unit"]
    wind_speed_unit = unit_dict["wind_speed_unit"]

    # 显示用户可见信息
    iterm = f"""
            城市:{city}
            日期:{date}
            日间天气:{text_day}
            晚间天气:{text_night}
            最高温度:{high_temp} {temp_unit}
            最低温度:{low_temp} {temp_unit}
            风向:{wind_direction}
            风速:{wind_speed} {wind_speed_unit}
            """
    print(iterm)
    return iterm

def unit_change(unit):
    """
    单位转换
    """
    if unit == "c":
        unit_dict = {
            "temp_unit":" °C",
            "wind_speed_unit":" km/h",
            "visbility_uint":" km",
            "presure_unit":" mb"
        }
    else:
        unit_dict = {
            "temp_unit":" °F",
            "wind_speed_unit":" mph",
            "visbility_uint":" mi",
            "presure_unit":" in"
        }

    return unit_dict

# def temp_trans(city_temp_c):
#     city_temp_f = (9 / 5) * int(city_temp_c) + 32
#     return city_temp_f




if __name__ == '__main__':
    get_API_daily("武汉",{},[])
