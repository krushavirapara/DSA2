def issafe(r,c,board):
    if r>=0 and r<len(board) and c>=0 and c<len(board) and board[r][c]==-1:
        return True
    return False
def helper(board,row,col,n,pos,drow,dcol):
    if pos == n*n:
        return True
        
    for i in range(8):
        nrow = row + drow[i]
        ncol = col + dcol[i]
        
        if issafe(nrow,ncol,board):
            board[nrow][ncol]=pos
            if helper(board,nrow,ncol,n,pos+1,drow,dcol):
                return True
            board[nrow][ncol]=-1
    return False
    
def knights(n):
    board = [[-1 for i in range(n)] for j in range(n)]
    pos = 1
    drow = [2, 1, -1, -2, -2, -1, 1, 2]
    dcol = [1, 2, 2, 1, -1, -2, -2, -1]
    board[0][0]=0
    helper(board,0,0,n,pos,drow,dcol)
    
    return board
print(knights(8))