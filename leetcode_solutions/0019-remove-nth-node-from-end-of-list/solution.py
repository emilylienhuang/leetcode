# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        tempHead = ListNode(-1)
        tempHead.next = head

        slow, fast = tempHead, tempHead
        position = 0
        while position <= n:
            fast = fast.next
            position += 1

        while fast:
            slow = slow.next
            fast = fast.next

        #remove the nth node: 
        slow.next = slow.next.next

        return tempHead.next
        

        
