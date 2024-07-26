def draw_stars(n):
    if n == 0:
        return
    
    draw_stars(n-1)
    print("*" * n)

N = int(input())
draw_stars(N)