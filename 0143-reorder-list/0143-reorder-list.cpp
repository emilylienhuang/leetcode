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
    void reorderList(ListNode* head) {
        /*
        1. Create a copy forwards and a copy backwards or reversed
        2. Iterate repeatedly alternating forward and backward into merged list
        3. There may be one element left if odd. Handle it
        bckwd = new node
        curr = head
        prev = None
        while curr and curr.next:
            next = curr.next
            curr.next = prev
         */
        if (!head) return;

        vector<ListNode*> nodes;
        ListNode* cur = head;
        while(cur){
            nodes.push_back(cur);
            cur = cur->next;
        }
        int i = 0;
        int j = nodes.size() - 1;
        while (i < j){
            nodes[i++]->next = nodes[j];
            if (i >= j) break;
            nodes[j--]->next = nodes[i];
        }
        nodes[i]->next= nullptr;
    }
};