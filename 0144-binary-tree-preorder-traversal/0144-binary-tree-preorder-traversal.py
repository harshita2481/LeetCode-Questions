# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        l=[]
        def trav(n):
            if not n:
                return 
            l.append(n.val)
            trav(n.left)
            trav(n.right)
        trav(root)
        return l