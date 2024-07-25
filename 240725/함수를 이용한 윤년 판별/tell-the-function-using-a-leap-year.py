def is_yoon(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 != 0:
                return "false"
        return "true"
    return "false"

y = int(input())

print(is_yoon(y))