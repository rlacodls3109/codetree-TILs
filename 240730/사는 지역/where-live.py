class People:
    def __init__(self,name,code,country):
        self.name = name
        self.code = code
        self.country = country

n = int(input())
peoples = []

for _ in range(n):
    name, code, country = tuple(input().split())
    peoples.append(People(name,code,country))

max = 0
idx = 0
for i in range(n):
    char = peoples[i].name[0]
    if max < int(ord(char)):
        max = int(ord(char))
        idx = i

people1 = peoples[idx]
print("name",people1.name)
print("addr",people1.code)
print("city",people1.country)