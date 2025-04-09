# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(left_node, right_node):
            if not left_node and not right_node:
                return True

            if not left_node or not right_node or left_node.val != right_node.val:
                return False
            
            left = dfs(left_node.left, right_node.right)
            right = dfs(left_node.right, right_node.left)
            return left and right
        
        return dfs(root.left, root.right)
