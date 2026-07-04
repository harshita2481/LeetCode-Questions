class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        def bt(ind,i,j):
            if ind==len(word):
                return True
            if i<0 or j<0 or i>=rows or j>=cols or word[ind]!=board[i][j]:
                return False
            temp=board[i][j]
            board[i][j]="#"
            found=bt(ind+1,i+1,j) or bt(ind+1,i-1,j) or bt(ind+1,i,j+1) or bt(ind+1,i,j-1)
            board[i][j]=temp
            return found
        for i in range(rows):
            for j in range(cols):
                if bt(0,i,j):
                    return True
        return False