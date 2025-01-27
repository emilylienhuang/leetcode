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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null){
            return list2;
        }
        if (list2 == null ){
            return list1;
        }
        ListNode tHead = new ListNode(-1);
        ListNode curr = tHead;
        ListNode c1 = list1;
        ListNode c2 = list2;
        while (c1 != null && c2 != null){
            if (c1.val < c2.val){
                curr.next = c1;
                c1 = c1.next;
            } else{
                curr.next = c2;
                c2 = c2.next;
            }
            curr = curr.next;
        }
        while (c1 != null){
            curr.next = c1;
            c1 = c1.next;
            curr = curr.next;
        }

        while (c2 != null){
            curr.next = c2;
            c2 = c2.next;
            curr = curr.next;
        }
        return tHead.next;
    }
}