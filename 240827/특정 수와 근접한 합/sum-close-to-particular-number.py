import sys

n, s = tuple(map(int,input().split()))
number_list = list(map(int,input().split()))
result = sys.maxsize

number_total = 0
for num in number_list:
    number_total += num

for i in range(n):
    for j in range(i,n):
        cal = number_total - number_list[i] - number_list[j]
        result = min(result,abs(s - cal))

print(result)