class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def bt(col,result,board,crow,cud,cld):
            if col==n:
                temp=["".join(row) for row in board]
                result.append(temp)
                return
            for row in range(n):
                if crow[row]==0 and cud[row+col]==0 and cld[row-col]==0:
                    board[row][col]='Q'
                    crow[row]=1
                    cud[row+col]=1
                    cld[row-col]=1
                    bt(col+1,result,board,crow,cud,cld)
                    crow[row]=0
                    cud[row+col]=0
                    cld[row-col]=0
                    board[row][col]='.'
        board=[['.' for i in range(n)] for i in range(n)]
        crow=[0]*n
        cud=[0]*(2*n-1)
        cld=[0]*(2*n-1)
        result=[]
        bt(0,result,board,crow,cud,cld)
        return result