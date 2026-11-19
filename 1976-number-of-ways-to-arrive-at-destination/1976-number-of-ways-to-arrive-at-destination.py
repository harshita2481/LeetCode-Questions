import heapq
class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        MOD=(10**9)+7
        ways=[0]*n
        dis=[float('inf')]*n
        dis[0]=0
        ways[0]=1
        adj=[[] for i in range(n)]
        for i in roads:
            adj[i[0]].append((i[1],i[2]))
            adj[i[1]].append((i[0],i[2]))
        pq=[(0,0)]
        while pq:
            d,node=heapq.heappop(pq)
            for i,w in adj[node]:
                if w+d<dis[i]:
                    dis[i]=w+d
                    ways[i]=ways[node]
                    heapq.heappush(pq,(dis[i],i))
                elif w+d==dis[i]:
                    ways[i]=(ways[i]+ways[node])%MOD
        if ways[n-1]==0:
            return -1
        return ways[n-1]%MOD


        