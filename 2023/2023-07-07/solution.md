# Solution - 07 Jul 2023

---
## [1. Add Two Numbers as Lists](https://workat.tech/problem-solving/practice/add-numbers-lists) [(LeetCode)](https://leetcode.com/problems/add-two-numbers/) 

### cpp
```cpp
/* This is the ListNode class definition

class ListNode {
public:
	int data;
	ListNode* next;

	ListNode(int data) {
		this->data = data;
		this->next = NULL;
	}
};
*/

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
	ListNode *ans = new ListNode(0), *cur = ans;
	int carry = 0;
	while(true) {
		if(!l1 && !l2 && !carry) break;
		int digit = carry;
		if(l1) digit += l1->data, l1 = l1->next;
		if(l2) digit += l2->data, l2 = l2->next;
		carry = digit/10;
		cur->next = new ListNode(digit%10);
		cur = cur->next;
	}
	return ans->next;
}
```


---
## [2. Reverse a Linked List II](https://workat.tech/problem-solving/practice/reverse-linked-list-ii) [(LeetCode)](https://leetcode.com/problems/reverse-linked-list-ii/) 

### cpp
```cpp
/* This is the ListNode class definition

class ListNode {
public:
	int data;
	ListNode* next;

	ListNode(int data) {
		this->data = data;
		this->next = NULL;
	}
};
*/
ListNode* reverseLinkedListRange(ListNode* head, int left, int right) {
	ListNode *dummy = new ListNode(0), *prev = dummy, *curr = NULL, *tmp;
	dummy->next = head;
	for(int i=1; i<left; i++)
		prev = prev->next;
	
	curr = prev->next;
	for(int i=0; i<right-left; i++) {
		tmp = prev->next;
		prev->next = curr->next;
		curr->next = curr->next->next;
		prev->next->next = tmp;
	}
	
	return dummy->next;
}
```
