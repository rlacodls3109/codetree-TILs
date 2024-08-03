# 이름, 키, 몸무게를 속성으로 가지는 class 선언

class Person:
    def __init__(self,name,h,w):
        self.name = name
        self.h = h
        self.w = w

# 첫번째줄에 n 입력받음
n = int(input())

# n줄에 걸쳐 이름, 키, 몸무게 받아 튜플형식으로 리스트로 저장
arr = [
    tuple(input().split())
    for _ in range(n)
]

# 리스트에 저장된 값을 클래스로 저장
people = [
    Person(name,int(h),int(w))
    for name,h,w in arr
]

#custom Comparator 사용 (키에 대해 오름차순, 몸무게 내림차순 정렬)
people.sort(key = lambda x : (x.h,-x.w))

#출력
for P in people:
    print(P.name,P.h,P.w)