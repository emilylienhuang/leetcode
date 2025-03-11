# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node_val = []
        cur = head
        while cur:
            node_val.append(cur.val)
            cur = cur.next
        
        max_sum = 0
        l, r = 0, len(node_val) - 1
        while l < r:
            max_sum = max(max_sum, node_val[l] + node_val[r])
            l += 1
            r -= 1
        return max_sum