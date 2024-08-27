arr = [
    list(map(int,input().split()))
    for _ in range(19)
]

def check_updown(x,y,color):
    return arr[x-1][y] == color and arr[x-2][y] == color and arr[x+1][y] == color and arr[x+2][y] == color

def check_side(x,y,color):
    return arr[x][y-1] == color and arr[x][y-2] == color and arr[x][y+1] == color and arr[x][y+2] == color

def check_diagonal(x,y,color):
    return arr[x-1][y-1] == color and arr[x-2][y-2] == color and arr[x+1][y+1] == color and arr[x+2][y+2] == color
for i in range(2,len(arr)-1):
    for j in range(2,len(arr[1])-1):
        if arr[i][j] != 0:
            color = arr[i][j]
            if check_side(i,j,color) or check_updown(i,j,color) or check_diagonal(i,j,color):
                print(color)
                print(i+1,j+1)