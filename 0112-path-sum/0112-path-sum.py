# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        dfs(root, 0)
        dfs(node, currSum):
            if not node and currSum == targetSum:
                return True
            elif not node:
                return False
            return dfs(node.left, currSum + node.val) or dfs(node.right, currSum + node.val)
        '''
        
        if not root:
            return False

        def dfs(node, currSum):
            if not node and currSum == targetSum:
                return True
            elif not node:
                return False
            return dfs(node.left, currSum + node.val) or dfs(node.right, currSum + node.val)
        return dfs(root, 0)