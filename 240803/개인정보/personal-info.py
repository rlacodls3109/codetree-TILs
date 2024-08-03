#이름,키,몸무게를 가지는 클래스 선언
class Personal:
    def __init__(self,name,h,w):
        self.name = name
        self.h = h
        self.w = w

#개인정보를 담을 리스트 선언
personals = []

#5줄에 걸쳐서 개인정보를 받는다.
#키, 몸무게는 int로 형변환한다.
for _ in range(5):
    x = tuple(input().split())
    personals.append(Personal(x[0],int(x[1]),float(x[2])))

#이름순으로 정렬
personals.sort(key = lambda x : x.name)

print("name")
for P in personals:
    print(P.name,P.h,P.w)

print()
#키 순으로 내림차순 정렬
personals.sort(key = lambda x : -x.h)

print("height")
for P in personals:
    print(P.name,P.h,P.w)