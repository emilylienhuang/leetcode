/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head.next == null){
            return null;
        }
        // put a fast pointer n + 1 ahead
        ListNode slow = head;
        ListNode fast = head;
        for (int i = 0; i < n + 1; i++){
            fast = fast.next;
        }
        
        // move fast to the end of the LL
        while (fast != null){
            slow = slow.next;
            fast = fast.next;
        }
        
        // slow .next = slow.next.next
        slow.next = slow.next.next;
        return head;
    }
}