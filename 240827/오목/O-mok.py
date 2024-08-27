arr = [
    list(map(int,input().split()))
    for _ in range(19)
]

def check_updown(x,y,color):
    return arr[x-1][y] == color and arr[x-2][y] == color and arr[x+1][y] == color and arr[x+2][y] == color

def check_side(x,y,color):
    return arr[x][y-1] == color and arr[x][y-2] == color and arr[x][y+1] == color and arr[x][y+2] == color

for i in range(2,len(arr)-1):
    for j in range(2,len(arr[1])-1):
        if arr[i][j] != 0:
            if check_side(i,j,arr[i][j]) or check_updown(i,j,arr[i][j]):
                print(arr[i][j])
                print(i,j)