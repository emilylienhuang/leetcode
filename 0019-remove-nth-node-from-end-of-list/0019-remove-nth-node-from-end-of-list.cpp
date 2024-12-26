/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        /*
        Intuition: use fasta nd slow pointers
        1. put exactly n + 1 spaces between fast and slow.
        2. Iterate until fast is pointed at nothing
        3. set slow->next = slow->next->next
        4. Return head 
        */
        if (!head) return nullptr;
        ListNode* dummy = new ListNode(-1, head);
        ListNode* slow = dummy;
        ListNode* fast = head;
        while (n > 0){
            fast = fast->next;
            n--;
        }
        while (fast){
            fast = fast->next;
            slow = slow->next;
        }
        slow->next = slow->next->next;
        return dummy->next;
    }
};