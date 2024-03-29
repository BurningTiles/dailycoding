# Solution - 23 May 2023

---
## [1. Middle Element of Linked List](https://workat.tech/problem-solving/practice/middle-element-linked-list) [(LeetCode)](https://leetcode.com/problems/middle-of-the-linked-list/) 

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

int getMiddleElementOfLinkedList (ListNode* list) {
	if(!list) return -1;
	ListNode *fast = list->next, *slow = list;
	while(fast && fast->next)
		fast = fast->next->next,
		slow = slow->next;
	return slow->data;
}
```

---
## [2. Merge Two Sorted Linked List](https://workat.tech/problem-solving/practice/merge-sorted-linked-list) [(LeetCode)](https://leetcode.com/problems/merge-two-sorted-lists/) 

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

ListNode* mergeTwoSortedList (ListNode* list1, ListNode* list2) {
	ListNode *head = new ListNode(0), *cur = head;
	while(list1 && list2) {
		if(list1->data <= list2->data)
			cur->next = list1, list1 = list1->next;
		else
			cur->next = list2, list2 = list2->next;
		cur = cur->next;
	}
	if(list1) cur->next = list1;
	if(list2) cur->next = list2;
	return head->next;
}
```