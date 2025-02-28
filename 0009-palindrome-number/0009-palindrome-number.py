class Node:
    def __init__(self, val):
        self.val = val
        self.prev, self.next = None, None
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # edge case
        if x < 0:
            # negative doesn't count
            return False
        
        if 0 <= x < 10:
            # single number is a palindrome
            return True
        
        '''
        We have a number in the double, triple, quadruple digits, etc
        We want to check if the number is the same fwd and reverse
        '''
        head = Node(-1)
        tail = Node(-1)
        head.next, tail.prev = tail, head
        curr = head
        
        while x:
            val = x % 10
            nextNode = Node(val)
            curr.next = nextNode
            nextNode.prev = curr
            tail.prev = nextNode
            curr = nextNode
            x = x // 10
        
        front, back = head, tail
        while front.next and back.prev and front != back:
            if front.val != back.val:
                return False
            front = front.next
            back = back.prev

        return True


        