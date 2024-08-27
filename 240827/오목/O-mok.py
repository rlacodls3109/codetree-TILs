arr = [
    list(map(int,input().split()))
    for _ in range(19)
]

def check_updown(x,y,color):
    return arr[x-1][y] == color and arr[x-2][y] == color and arr[x+1][y] == color and arr[x+2][y] == color

def check_side(x,y,color):
    return arr[x][y-1] == color and arr[x][y-2] == color and arr[x][y+1] == color and arr[x][y+2] == color

def check_Rdiagonal(x,y,color):
    return arr[x-1][y-1] == color and arr[x-2][y-2] == color and arr[x+1][y+1] == color and arr[x+2][y+2] == color

def check_Ldiagonal(x,y,color):
    return arr[x-1][y+1] == color and arr[x-2][y+2] == color and arr[x+1][y-1] == color and arr[x+2][y-2] == color

winner = 0

for i in range(2,len(arr)-1):
    for j in range(2,len(arr[1])-1):
        if arr[i][j] != 0:
            color = arr[i][j]
            if check_side(i,j,color) or check_updown(i,j,color) or check_Rdiagonal(i,j,color) or check_Ldiagonal(i,j,color):
                winner = color
                winner_pos_x, winner_pos_y = i+1, j+1

if winner == 0:
    print(winner)
else :
    print(winner)
    print(winner_pos_x,winner_pos_y)