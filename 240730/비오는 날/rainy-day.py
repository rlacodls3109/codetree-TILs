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

min = 2100
idx = 0

for i in range(n):
    if weathers[i].weather == "Rain":
        y = int(weathers[i].date.split("-")[0])

        if min > y:
            min = y
            idx = i

print(weathers[idx].date, weathers[idx].weekday, weathers[idx].weather)