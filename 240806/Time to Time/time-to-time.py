a,b,c,d = tuple(map(int,input().split()))

start_min = a*60 + b
end_min = c*60 + d

answer = end_min - start_min

print(answer)