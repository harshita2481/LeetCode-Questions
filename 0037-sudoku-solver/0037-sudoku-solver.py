class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=[set() for i in range(9)]
        cols=[set() for i in range(9)]
        boxes=[set() for i in range(9)]
        empties=[]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    empties.append((i,j))
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[3*(i//3)+(j//3)].add(board[i][j])
        def solve(board,index,empties,rows,cols,boxes):
            if index==len(empties):
                return True
            i,j=empties[index]
            b=3*(i//3)+(j//3)
            for c in "123456789":
                if c not in rows[i] and c not in cols[j] and c not in boxes[b]:
                    board[i][j]=c
                    rows[i].add(c)
                    cols[j].add(c)
                    boxes[b].add(c)
                    if solve(board,index+1,empties,rows,cols,boxes):
                        return True
                    board[i][j]='.'
                    rows[i].remove(c)
                    cols[j].remove(c)
                    boxes[b].remove(c)
            return False
        solve(board,0,empties,rows,cols,boxes)