# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid_point = inorder.index(preorder[0])
        leftSide = self.buildTree(preorder[1:mid_point + 1], inorder[:mid_point])
        rightSide = self.buildTree(preorder[mid_point + 1: ], inorder[mid_point + 1 :])
        root.left = leftSide
        root.right = rightSide
        return root