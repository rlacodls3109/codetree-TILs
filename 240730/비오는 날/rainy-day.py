from datetime import datetime

class Weather:
    def __init__(self,date,weekday,weather):
        self.date = datetime.strptime(date, '%Y-%m-%d').date()
        self.weekday = weekday
        self.weather = weather

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
weathers = [
    Weather(date,weekday,weather) 
    for date,weekday,weather in arr
]

min_date = datetime.strptime("2100-12-31",'%Y-%m-%d').date()
idx = 0

for i in range(n):
    if weathers[i].weather == "Rain":
        if min_date > weathers[i].date:
            min_date = weathers[i].date
            idx = i

print(weathers[idx].date, weathers[idx].weekday, weathers[idx].weather)