def draw_star(n):
    if n == 0 :
        return
    
    print("*"*n)
    draw_star(n-1)
    print("*"*n)

N = int(input())
draw_star(N)