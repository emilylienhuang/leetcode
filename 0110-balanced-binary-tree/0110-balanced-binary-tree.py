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
                return [0, True]
            
            lDist, lBal = dfs(node.left)
            rDist, rBal = dfs(node.right)

            bal = rBal and lBal and abs(lDist - rDist) <= 1
            
            return [max(lDist,rDist) + 1, bal]
        
        return dfs(root)[1]
