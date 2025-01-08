# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return [True, 0]
            
            leftEval, leftDepth = dfs(node.left)
            rightEval, rightDepth = dfs(node.right)

            balanced = leftEval and rightEval and abs(leftDepth - rightDepth) <= 1
            return [balanced, max(leftDepth, rightDepth) + 1]
        return dfs(root)[0]