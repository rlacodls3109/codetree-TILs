def is_yoon(y):
    if y % 4 != 0:
        return "false"
    if y % 100 != 0:
        return "true"
    if y % 400 != 0:
        return "false"
    return "true"

y = int(input())

print(is_yoon(y))