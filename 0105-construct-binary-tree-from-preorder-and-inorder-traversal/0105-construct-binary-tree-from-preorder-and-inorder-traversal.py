class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        total = len(preorder)
        return self.build(preorder, inorder, 0, 0, total - 1)

    def build(self, preorder, inorder, preStart, inStart, inEnd):
        if inStart > inEnd:
            return None

        rootValue = preorder[preStart]
        root = TreeNode(rootValue)

        rootIndex = inStart
        while inorder[rootIndex] != rootValue:
            rootIndex = rootIndex + 1

        leftSize = rootIndex - inStart

        leftPreStart = preStart + 1
        leftInStart = inStart
        leftInEnd = rootIndex - 1
        root.left = self.build(preorder, inorder, leftPreStart, leftInStart, leftInEnd)

        rightPreStart = preStart + 1 + leftSize
        rightInStart = rootIndex + 1
        rightInEnd = inEnd
        root.right = self.build(preorder, inorder, rightPreStart, rightInStart, rightInEnd)

        return root