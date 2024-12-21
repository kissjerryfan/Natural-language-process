def get_weather_forecast():
    """
        Get the current weather and 9-day weather forecast from the Hong Kong Observatory.
        Args:
           None

        Returns:
           None
    """
    import requests
    api_url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php"
    
    forecast_params = {
        'dataType': 'fnd',  
        'lang': 'tc'  
    }
    
    current_weather_params = {
        'dataType': 'rhrread',  
        'lang': 'tc'
    }

    forecast_response = requests.get(api_url, params=forecast_params)
    current_weather_response = requests.get(api_url, params=current_weather_params)
    
    if forecast_response.status_code == 200 and current_weather_response.status_code == 200:
        forecast_data = forecast_response.json()
        current_weather_data = current_weather_response.json()

        print("九天天气预报：")
        for day in forecast_data['weatherForecast']:
            print(f"日期: {day['forecastDate']}")
            print(f"天气: {day['forecastWeather']}")
            print(f"最高温度: {day['forecastMaxtemp']['value']}°C")
            print(f"最低温度: {day['forecastMintemp']['value']}°C")
            print(f"相对湿度: {day['forecastMaxrh']['value']}% - {day['forecastMinrh']['value']}%")
            print(f"风速: {day['forecastWind']}")
            print("--------------------")

        print("当前天气：")
        print("温度：", current_weather_data['temperature']['data'][0]['value'], "°C")
        print("湿度：", current_weather_data['humidity']['data'][0]['value'], "%")
        print("天气情况：", current_weather_data['icon'][0])

    else:
        print("无法获取天气数据")

get_weather_forecast()
