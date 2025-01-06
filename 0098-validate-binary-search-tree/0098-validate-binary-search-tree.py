# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, leftWeight, rightWeight):
            if not root:
                return True
            if leftWeight > root.val or rightWeight < root.val:
                return False
            if leftWeight < root.val < rightWeight:
                return dfs(root.left, leftWeight, root.val) and dfs(root.right, root.val, rightWeight)
        
        return dfs(root, float('-inf'), float('inf'))