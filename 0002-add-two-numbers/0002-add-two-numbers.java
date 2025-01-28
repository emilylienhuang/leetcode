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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode tHead = new ListNode(-1);
        ListNode curr = tHead;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0){
            int digit1 = l1 == null ? 0 : l1.val;
            int digit2 = l2 == null ? 0 : l2.val;

            int total = digit1 + digit2 + carry;
            int num = total % 10;
            carry = total / 10;
            ListNode newNode = new ListNode(num);
            curr.next = newNode;
            curr = curr.next;
            if (l1 != null){
                l1 = l1.next;
            }
            if (l2 != null){
                l2 = l2.next;
            }
        }
        return tHead.next;
    }
    }