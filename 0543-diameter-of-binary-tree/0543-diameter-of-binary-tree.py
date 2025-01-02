# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        calls for: dfs
        start from root 
        if root.left and root.right:
            1 + curr_diameter
            recursively call 
        else
        update max diameter
        '''

        max_diameter = 0

        def dfs(root):
            if not root:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)

            nonlocal max_diameter
            max_diameter = max(max_diameter, r + l)
            return 1 + max(l, r)
        dfs(root)
        return max_diameter
        