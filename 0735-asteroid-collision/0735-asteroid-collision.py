class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in range(len(asteroids)):
            if asteroids[i]>0:
                stack.append(asteroids[i])
            else:
                while stack and stack[-1]>0 and asteroids[i]<0 and stack[-1]<abs(asteroids[i]):
                    stack.pop()
                if stack and abs(asteroids[i])==stack[-1]:
                    stack.pop()
                else:
                    if not stack or stack[-1]<0:
                        stack.append(asteroids[i])
        return stack
            
            