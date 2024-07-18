# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Time Complexity: O(n)
        # Space Complexity O(1) because we did no allocation for a new data structure
        #edge case checks:
        if (not head or (head.next == None)):
            return head

        #plan: two pointers: one for even and one for odd
        # then, fuse the pointers together and return the odd head

        #Step One: initialize oddList to head and evenList to head.next
        oddList, evenList = head, head.next
        evenHead = evenList
        
        #[1,2,3,4,5]
        while oddList.next and evenList.next:  # even.next check for the odd value to hold something not None
            #if evenList.next == None
            oddList.next = oddList.next.next # 1 -> 3
            evenList.next = evenList.next.next # 2 -> 4

            oddList = oddList.next
            evenList = evenList.next

        # odd: 1->3->5
        # even: 2->4
        oddList.next = evenHead

        # if you think about it here, the head is still preserved only its
        #references have been changed by the moving odd pointer
        return head

        
         

