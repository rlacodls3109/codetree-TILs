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

idx = 0

name_list = [
    peoples[i].name
    for i in range(n)
]

name_list.sort()

for i in range(n):
    if name_list[-1] == peoples[i].name:
        idx = i
        break
    
people1 = peoples[idx]
print("name",people1.name)
print("addr",people1.code)
print("city",people1.country)



'''
이런 방법도 되는군..
class Address:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region
        
        
# 변수 선언 및 입력
n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
people = [Address(name, address, region) for name, address, region in arr]

# 사전순으로 이름이 가장 느린 사람 찾기
target_idx = 0
for i, person in enumerate(people):
    if person.name > people[target_idx].name:
        target_idx = i

# 결과 출력
print(f"name {people[target_idx].name}")
print(f"addr {people[target_idx].address}")
print(f"city {people[target_idx].region}")
'''