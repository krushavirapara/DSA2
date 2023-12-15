def queens(board,row):
    if row==len(board):
        display(board)
        print()
        return 1
    else:
        count=0
        for col in range(len(board)):
            if isSafe(board,row,col):
                board[row][col]="Q"
                count+=queens(board,row+1)
                board[row][col]=0
        return count
        
def isSafe(board,row,col):
    for i in range(row):
        if board[i][col]:
            return False
    
    left = min(row,col)
    for i in range(1,left+1):
        if board[row-i][col-i]:
            return False
            
    right = min(row,len(board)-col-1)
    for i in range(1,right+1):
        if board[row-i][col+i]:
            return False
    return True

board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def display(board):
    for i in board:
        for j in i:
            print(j,end="")
        print()
       
    
print(queens(board,0))