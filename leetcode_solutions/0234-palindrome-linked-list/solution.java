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
    public boolean isPalindrome(ListNode head) {
        List<Integer> values = new ArrayList<>();
        ListNode traverser = head;
        while (traverser != null){
            values.add(traverser.val);
            traverser = traverser.next;
        }

        int l = 0;
        int r = values.size() - 1;
        while (l < r){
            if (values.get(l) != values.get(r)){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}
