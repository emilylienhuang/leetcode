# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            leftBal, leftDepth = dfs(root.left)
            rightBal, rightDepth = dfs(root.right)
            balanced = leftBal and rightBal and abs(leftDepth - rightDepth) <= 1
            return [balanced, 1 + max(leftDepth, rightDepth)]
            
        bal, _ = dfs(root)
        return bal