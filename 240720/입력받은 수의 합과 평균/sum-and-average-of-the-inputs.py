n = int(input())
sum = 0
for i in range(n):
    num = int(input())
    sum += num

avg = sum / n

print(f"{sum} {avg:.1f}")