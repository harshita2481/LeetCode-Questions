class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def check(col,row,board):
            for i in range(col):
                if board[row][i]=='Q':
                    return False
            i=row
            j=col
            while i>=0 and j>=0:
                if board[i][j]=='Q':
                    return False
                i-=1
                j-=1
            i=row
            j=col
            while i<n and j>=0:
                if board[i][j]=='Q':
                    return False
                i+=1
                j-=1
            return True
        def bt(board,col,result):
            if col==n:
                temp=["".join(row) for row in board]
                result.append(temp)
                return 
            for row in range(n):
                if check(col,row,board):
                    board[row][col]='Q'
                    bt(board,col+1,result)
                    board[row][col]='.'

        board=[['.' for i in range(n)]for i in range(n)]
        result=[]
        bt(board,0,result)
        return result
