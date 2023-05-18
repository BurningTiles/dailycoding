# Solution - 17 May 2023

---
## [1. Linked List to Array](https://workat.tech/problem-solving/practice/linked-list-to-array) 

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

vector<int> linkedListToArray (ListNode* head) {
	vector<int> ans;
	while(head)
		ans.push_back(head->data), head = head->next;
	return ans;
}
```

---
## [2. Print Reversed Linked List](https://workat.tech/problem-solving/practice/print-reversed-linked-list) 

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

void printLinkedListReverse (ListNode* head) {
	if(head) {
		printLinkedListReverse(head->next);
		cout << head->data << " ";
	}
}
```