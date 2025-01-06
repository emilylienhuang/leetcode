# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(root):
            if not root:
                return [True, 0]
            
            leftEval, leftDepth = dfs(root.left)
            rightEval, rightDepth = dfs(root.right)

            balanced = leftEval and rightEval and abs(leftDepth - rightDepth) <= 1
            return [balanced, max(leftDepth, rightDepth) + 1]
        evaluation, depth = dfs(root)
        return evaluation

