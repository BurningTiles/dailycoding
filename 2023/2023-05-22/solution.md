# Solution - 22 May 2023

---
## [1. Reverse a Linked List](https://workat.tech/problem-solving/practice/reverse-linked-list) [(LeetCode)](https://leetcode.com/problems/reverse-linked-list/) 

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

ListNode* reverseLinkedList (ListNode* head) {
	ListNode *cur = head, *prev = NULL, *next = NULL;
	while(cur) {
		next = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next;
	}
	head = prev;
	return head;
}

/*
// Recursive method
ListNode* reverseLinkedList (ListNode* head, ListNode* parent=NULL) {
	if(head) {
		ListNode *tmp = reverseLinkedList(head->next, head);
		head->next = parent;
		if(tmp) head = tmp;
	}
	return head;
}
*/
```

---
## [2. Remove occurrences in Linked List](https://workat.tech/problem-solving/practice/remove-occurences-linked-list) [(LeetCode)](https://leetcode.com/problems/remove-linked-list-elements/) 

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
ListNode* removeOccurences(ListNode* head, int key) {
	while(head && head->data == key)
		head = head->next;
	ListNode *ptr = head;
	while(ptr && ptr->next) {
		if(ptr->next->data==key)
			ptr->next = ptr->next->next;
		else
			ptr = ptr->next;
	}
	return head;
}
```