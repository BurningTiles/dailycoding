# Solution - 19 May 2023

---
## [1. Remove Element at Kth Position in Linked List](https://workat.tech/problem-solving/practice/delete-kth-element-linked-list) 

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


ListNode* removekthElement (ListNode* head, int k) {
	if(k==1) return head->next;
	ListNode *ptr = head;
	int i=k-1;
	while(--i)
		ptr = ptr->next;
	ptr->next = ptr->next->next;
	return head;
}


/*
// Another solution with better memory management.
ListNode* removekthElement (ListNode* head, int k) {
	ListNode *tmp;
	if(k==1) {
		tmp = head;
		head = head->next;
		delete tmp;
		return head;
	}
	ListNode *ptr = head;
	int i = k-1;
	while(--i)
		ptr = ptr->next;
	tmp = ptr->next;
	ptr->next = tmp->next;
	delete tmp;
	return head;
}
*/
```

---
## [2. Append Linked Lists](https://workat.tech/problem-solving/practice/append-linked-lists) 

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

ListNode* appendLists (ListNode* list1, ListNode* list2) {
	if(!list1) return list2;
	ListNode *ptr = list1;
	while(ptr->next)
		ptr = ptr->next;
	ptr->next = list2;
	return list1;
}
```