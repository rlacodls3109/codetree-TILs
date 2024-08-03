#인덱스와 숫자를 가지는 클래스 선언
class Number:
    def __init__(self,index,number):
        self.index=index
        self.number=number

n = int(input())

#숫자 배열 입력받음
num = tuple(map(int,input().split()))

#초기 위치와 숫자 정보를 가지는 number 배열 선언 후 값 추가
number = []
for i,k in enumerate(num):
    number.append(Number(i+1,k))

#custom comparator (숫자 오름차순, 인덱스 오름차순)
number.sort(key = lambda x: (x.number,x.index))

position = [0]*n

for i,N in enumerate(number,start=1):
    position[N.index-1] = i

for elem in position:
    print(elem,end=" ")