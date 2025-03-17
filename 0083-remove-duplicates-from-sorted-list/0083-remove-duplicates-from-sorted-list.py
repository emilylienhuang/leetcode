# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        tHead = ListNode(-1)
        tHead.next = head
        curr = head
        while curr:
            nxt = curr.next
            while nxt and nxt.val == curr.val:
                nxt = nxt.next
            curr.next = nxt
            curr = curr.next
        
        return tHead.next
