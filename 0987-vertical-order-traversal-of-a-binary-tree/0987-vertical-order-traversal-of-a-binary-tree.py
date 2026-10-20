# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        ans=[]
        if not root:
            return []
        q=deque()
        q.append([root,0,0])
        d={0:[(root.val,0)]}
        while q:
            for _ in range(len(q)):
                n=q.popleft()
                node=n[0]
                level=n[2]
                vert=n[1]
                if node.left:
                    q.append([node.left,vert-1,level+1])
                    if vert-1 in d:
                        d[vert-1].append((node.left.val,level+1))
                    else:
                        d[vert-1]=[(node.left.val,level+1)]
                if node.right:
                    q.append([node.right,vert+1,level+1])
                    if vert+1 in d:
                        d[vert+1].append((node.right.val,level+1))
                    else:
                        d[vert+1]=[(node.right.val,level+1)]
        for col in sorted(d):
            d[col].sort(key=lambda x:(x[1],x[0]))
            ans.append([i[0] for i in d[col]])
        return ans