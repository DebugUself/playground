import requests
from utils.const_value import API_NOW, KEY, LANGUAGE, \
                              API_DAILY, START, DAYS, \
                              OWM_API,OWM_APIKEY,OWM_ID


def test():
    print("ok!")

def get_API_now(unit, city, history_list):
    """
    NowMode:发送 now_api 请求, 对响应进行判断处理,  显示天气, 添加至历史记录
    """
    print("get_API NOW begin!")
    seniverse_param = seniverse_params(unit, city)
    weather_josn = get_response(seniverse_param, API_NOW)
    if weather_josn != None:
        iterm = josn_now_deal(unit, weather_josn)
        history_list.append(iterm)
    else:
        print("please check weather_josn")

def get_API_daily(unit, city_num_list, history_list):
    """
    DailyMode:发送 daily_api 请求, 对响应进行判断处理,  显示天气, 添加至历史记录
    """
    city = city_num_list[0]
    day_num = city_num_list[1]

    print("get_API_daily begin!")
    seniverse_param = seniverse_params(unit, city)
    weather_josn = get_response(seniverse_param, API_DAILY)

    if weather_josn != None:
        iterm = josn_daily_deal(unit, weather_josn, day_num)
        history_list.append(iterm)
    else:
        print("please check weather_josn")

def seniverse_params(unit,city):
    """
    心知天气 api 请求所需参数
    """
    seniverse_params = {
        'key' : KEY,
        'location' : city,
        'language' : LANGUAGE,
        'unit' : unit
    }
    return seniverse_params

def get_response(params,API):
    """
    发送API请求, 对响应进行判断
    """
    print("正在发生请求获取响应...")
    response = requests.get(
        API, params = params, timeout = 20)  # 向 API 发送请求了
    #print(response.url)
    if response.status_code == 200:  #请求成功, 打印相应天气信息并记录历史
        print("API 请求成功!")
        return response.json()
    elif response.status_code == 404:  #未找到城市信息, 用户重新输入
        print (response.status_code, '对不起, 无该城市天气信息, 请检查您的输入, 或者查询其他城市...')
    else:
        print('抱歉, 网络请求错误, 请重试...')  #其他错误代码


def josn_now_deal(unit, weather_josn):
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

def josn_daily_deal(unit, weather_josn, day_num):
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
            城市: {city}
            日期: {date}
            日间天气: {text_day}
            晚间天气: {text_night}
            最高温度: {high_temp} {temp_unit}
            最低温度: {low_temp} {temp_unit}
            风向: {wind_direction}
            风速: {wind_speed} {wind_speed_unit}
            """
    print(iterm)
    return iterm

def unit_change(unit):
    """
    单位转换
    """
    if unit == "c":
        unit_dict = {
            "temp_unit": "°C",
            "wind_speed_unit": "km/h",
            "visbility_uint": "km",
            "pressure_unit": "mb"
        }
    else:
        unit_dict = {
            "temp_unit": "°F",
            "wind_speed_unit": "mph",
            "visbility_uint": "mi",
            "pressure_unit": "in"
        }

    return unit_dict

# def temp_trans(city_temp_c):
#     city_temp_f = (9 / 5) * int(city_temp_c) + 32
#     return city_temp_f

def get_owm_weather_now(unit, city, history_list):
    """
    获取owm 的即时天气信息
    """
    print("get_owm_weather_now begin!")
    owm_param = owm_params(city,unit)
    weather_josn = get_response(owm_param, OWM_API)
    if weather_josn != None:
        iterm = handle_owm_now_josn(weather_josn,unit)
        history_list.append(iterm)
    else:
        print("please check weather_josn")

def owm_params(city, unit):
    print("正在获取参数...")
    unit_meaning = {'c': 'metric', 'f':'imperial' }
    owm_params = {
        'ID': OWM_ID,
        'APPID': OWM_APIKEY,
        'q': city,
        'lang': 'zh_cn',
        'units':unit_meaning[unit]
    }
    return owm_params

def handle_owm_now_josn(weather_josn, unit):
    print(weather_josn)
    visibility = " "
    try:
        city = weather_josn['name']
        temp = weather_josn['main']['temp']
        temp_min = weather_josn['main']['temp_min']
        temp_max = weather_josn['main']['temp_max']
        pressure = weather_josn['main']['pressure']
        humidity = weather_josn['main']['humidity']
        # visibility = weather_josn['visibility']
        wind_speed = weather_josn['wind']['speed']


        # 提取 单位信息
        unit_dict = unit_change(unit)
        temp_unit = unit_dict["temp_unit"]

        iterm = f"""
                city: {city}
                now_temp: {temp} {temp_unit}
                temp_max: {temp_max} {temp_unit}
                temp_min: {temp_min} {temp_unit}
                pressure: {pressure} hPa
                humidity: {humidity} %
                 visibility: {visibility} m
                wind_speed: {wind_speed} mps
                """
        print(iterm)
        return iterm

    except KeyError as e:
        print("KeyError",e )
    except UnboundLocalError as e:
        print("UnboundLocalError",e)






