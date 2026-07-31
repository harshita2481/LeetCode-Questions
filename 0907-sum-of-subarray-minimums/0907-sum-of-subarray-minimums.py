class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD=(10**9)+7
        n=len(arr)
        def nse(arr):
            nsel=[-1]*n
            stack=[]
            for i in range(n-1,-1,-1):
                while stack and arr[stack[-1]]>=arr[i]:
                    stack.pop()
                if stack:
                    nsel[i]=stack[-1]
                else:
                    nsel[i]=n
                stack.append(i)
            return nsel
        def pse(arr):
            stack=[]
            psel=[-1]*n
            for i in range(n):
                while stack and arr[stack[-1]]>arr[i]:
                    stack.pop()
                if stack:
                    psel[i]=stack[-1]
                else:
                    psel[i]=-1
                stack.append(i)
            return psel
        psel=pse(arr)
        nsel=nse(arr)
        total=0
        for i in range(n):
            total+=(nsel[i]-i)*(i-psel[i])*arr[i]
        return total%MOD