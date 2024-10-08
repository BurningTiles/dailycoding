# Solution - 06 Sep 2024

---
## [3217. Delete Nodes From Linked List Present in Array](https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array)

### cpp
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        unordered_set<int> uset(nums.begin(), nums.end());
        ListNode *ans = new ListNode(-1, head), *prev=ans;

        while(head) {
            if(uset.count(head->val))
                prev->next = head->next, head = head->next;
            else
                prev = head, head = head->next;
        }

        return ans->next;
    }
};
```
