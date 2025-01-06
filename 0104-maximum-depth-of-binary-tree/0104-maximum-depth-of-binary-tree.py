# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        maxDepth = 0
        def dfs(root, depth):
            if not root:
                return 0
            nonlocal maxDepth
            maxDepth = max(depth + 1, maxDepth)

            return 1 + max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
            
        maxDepth = dfs(root, 1)
        return maxDepth
