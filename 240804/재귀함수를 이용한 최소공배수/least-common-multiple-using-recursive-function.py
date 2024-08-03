#최대공약수(gcd) 구하기(유클리드 호제법)
def gcd(a,b):
    if a % b == 0:
        return b
    else :
        r = a % b
        return gcd(b,r) 

# 유클리드호제법을 통한 최소공배수 구하기
# lcm(a,b) = (a*b) / gcd(a,b)
def lcm(a,b):
    return (a * b) / gcd(a,b)

# 만약 배열의 길이가 1이라면 그 값 자체가 최대공배수가 된다.
# 배열의 앞쪽부터 두수의 최소 공배수를 구하고, 그 최소공배수와 다음 값의 최소공배수를 구하는 방식
def solution(arr,k):
    if k-1 == 0:
        return arr[0]
    else :
        return lcm(arr[k-1],solution(arr,k-1))

n = int(input())
arr = list(map(int,input().split()))

lcm = int(solution(arr,n))

print(lcm)