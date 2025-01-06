# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_diameter = 0
        def dfs(root):
            if not root:
                return 0
            
            left_dist = dfs(root.left)
            right_dist = dfs(root.right)

            nonlocal max_diameter
            max_diameter = max(left_dist + right_dist, max_diameter)

            return 1 + max(left_dist, right_dist)
        dfs(root)
        return max_diameter
