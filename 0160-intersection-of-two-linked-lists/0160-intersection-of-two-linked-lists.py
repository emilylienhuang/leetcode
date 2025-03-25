# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        cA = headA
        cB = headB

        while cA:
            seen.add(cA)
            cA = cA.next
        
        while cB:
            if cB in seen:
                return cB
            seen.add(cB)
            cB = cB.next
        return None