# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        '''
            if not root:
                # impossible to get to any sum
                return []
            
            res = []
            def dfs(node, seen):
                if not node and sum(seen) == targetSum:
                    # reached a leaf and found my sum
                    res.append(seen)
                    return 
                if not node:
                    # I've just reached a leaf and not my sum
                    return
                
                #include the current node and dfs
                seen.append(node.val)
                dfs(node.left)
                dfs(node.right)

                # exclude the current node and dfs
                seen.pop()
                dfs(node.left)
                dfs(node.right)
        '''

        if not root:
                # impossible to get to any sum
                return []
            
        res = []
        def dfs(node, seen, currSum):
            if not node:
                return
            seen.append(node.val)
            currSum += node.val
            
            if not node.left and not node.right and currSum == targetSum:
                res.append(seen[:])
                return 
            
            dfs(node.left, seen.copy(), currSum)
            dfs(node.right, seen.copy(), currSum)
            
        dfs(root, [], 0)
        return list(res)