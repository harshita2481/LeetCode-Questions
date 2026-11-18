from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dis=[[float('inf') for i in range(m)] for i in range(n)]
        dis[0][0]=1
        q=deque()
        if grid[0][0]!=0:
            return -1
        q.append(((0,0),1))
        dr=[1,0,-1,0,-1,-1,1,1]
        dc=[0,1,0,-1,1,-1,1,-1]
        while q:
            t=q.popleft()
            row=t[0][0]
            col=t[0][1]
            d=t[1]
            if d>dis[row][col]:
                continue
            for i in range(len(dr)):
                nr=row+dr[i]
                nc=col+dc[i]
                if 0<=nr<n and 0<=nc<m and dis[nr][nc]>d+1 and grid[nr][nc]==0:
                    dis[nr][nc]=d+1
                    q.append(((nr,nc),d+1))
        if dis[n-1][m-1]==float('inf'):
            return -1
        return dis[n-1][m-1]



        