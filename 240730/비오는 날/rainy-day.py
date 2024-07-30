from datetime import datetime

class Weather:
    def __init__(self,date,weekday,weather):
        self.date = date
        self.weekday = weekday
        self.weather = weather

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
weathers = [
    Weather(date,weekday,weather) 
    for date,weekday,weather in arr
]

min_date = "9999-99-99"
idx = 0

for i in range(n):
    if weathers[i].weather == "Rain":
        if min_date > weathers[i].date:
            min_date = weathers[i].date
            idx = i

print(weathers[idx].date, weathers[idx].weekday, weathers[idx].weather)