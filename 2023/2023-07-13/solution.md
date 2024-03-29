# Solution - 13 Jul 2023

---
## [1. Partition List](https://workat.tech/problem-solving/practice/partition-list) [(LeetCode)](https://leetcode.com/problems/partition-list/) 

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

ListNode* partitionList(ListNode* head, int key) {
	ListNode *left = new ListNode(0),  
		*mid = new ListNode(0), 
		*right = new ListNode(0);
	ListNode *l = left, *m = mid, *r = right;
	while(head) {
		if(head->data == key)
			m->next = head, m = head;
		else if(head->data < key)
			l->next = head, l = head;
		else
			r->next = head, r = head;
		head = head->next;
	}
	r->next = NULL;
	m->next = right->next;
	l->next = mid->next;
	return left->next;
}
```


---
## [2. Insertion Sort Linked List](https://workat.tech/problem-solving/practice/insertion-sort-linked-list) [(LeetCode)](https://leetcode.com/problems/insertion-sort-list/) 

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
ListNode* insertionSort(ListNode* head) {
	ListNode *list = new ListNode(0), *curr = head, *prev=list;
	list->next = head;
	while(curr) {
		ListNode *tmp = list, *next = curr->next;
		while(tmp->next->data < curr->data)
			tmp = tmp->next;
		if(tmp->next != curr) {
			curr->next = tmp->next;
			tmp->next = curr;
			prev->next = next;
		} else
			prev = curr;
		curr = next;
	}
	return list->next;
}
```
