# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = root.val
        max_level = 1
        level = 1

        q = deque()
        q.append(root)

        while q:
            level_count = len(q)
            curr_sum = 0
            for _ in range(level_count):
                node = q.popleft()
                curr_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if curr_sum > max_sum:
                max_level = level
                max_sum = curr_sum
            level += 1
        return max_level