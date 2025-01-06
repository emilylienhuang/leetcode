# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root, subRoot):
            if not root:
                return False
            if not subRoot:
                return True
            
            if root.val == subRoot.val:
                return self.sameTree(root, subRoot)
            
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        return dfs(root, subRoot)
    
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root:
            return False
        if not subRoot:
            return False
        
        if root.val != subRoot.val:
            return False
        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)