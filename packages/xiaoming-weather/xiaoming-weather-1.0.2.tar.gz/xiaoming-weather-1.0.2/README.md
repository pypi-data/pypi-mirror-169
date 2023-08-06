# Xiaoming-weather
Xiaoming weather provides personalized weather data strings for chinese user. Its weather data is captured from http://www.weather.com.cn

## Usage
Following query on terminal will provide you the weather details of the city you provided by option city code. You can get your city code in the URL by finding the city name on http://www.weather.com.cn. For example, China city ChongQing homepage is http://www.weather.com.cn/weather/101040100.shtml, the city code is 101040100.

```
zhangyd@zhangyd-ubuntu:~$ xiaoming-weather -q 101160407
小明天气：今天17℃~24℃，明天阴转多云，比今天凉一点，似乎要降温了。
明天: 阴转多云
温度: 10℃~20℃
风力: 3-4级转<3级
```
## Help
```
zhangyd@zhangyd-ubuntu:~$ xiaoming-weather --help
usage: xiaoming-weather [-h] [-q city-code]

XiaoMing Weather

optional arguments:
  -h, --help            show this help message and exit
  -q city-code, --query city-code
                        The specific city code from http://www.weather.com.cn
```