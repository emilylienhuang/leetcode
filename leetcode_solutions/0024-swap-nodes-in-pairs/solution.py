# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #edge cases
        if not head or not head.next:
            return head
        
        tHead = ListNode(-1)
        tHead.next = head

        # 1 -> 2 -> 3 -> 4
        # Need a pointer for the 1. previous pair, current, next node, next pair
        previous = tHead
        current = head

        while current and current.next:
            #find the next pair
            nextPair = current.next.next
            nextNode = current.next
            
            # swapping
            current.next = nextPair
            nextNode.next = current
            previous.next = nextNode

            previous = current
            current = nextPair

        return tHead.next
