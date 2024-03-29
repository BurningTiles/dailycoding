# Solution - 26 May 2023

---
## [1. Implement Stack using Array](https://workat.tech/problem-solving/practice/implement-stack-array) [(LeetCode)](https://leetcode.com/problems/design-a-stack-with-increment-operation/) 

```cpp
// Implement the Stack class
class Stack {
private:
	int *arr, ptr=0, capacity=0;
public:
	
	Stack (int capacity) {
		this->capacity = capacity;
		arr = new int[capacity];
	}

	bool isEmpty() {
		return ptr==0;
	}
	
	int size() {
		return ptr;
	}
	
	int top() {
		return ptr ? arr[ptr-1] : -1;
	}
	
	void push(int element) {
		if(ptr<capacity) arr[ptr++] = element;
	}
	
	void pop() {
		if(ptr) --ptr;
	}
};
```

---
## [2. Implement Stack using Linked List](https://workat.tech/problem-solving/practice/implement-stack-linked-list) 

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

// Implement the Stack class
class Stack {
private:
	ListNode *head=NULL;
	int _size=0, _capacity=0;
public:
	
	Stack (int capacity) {
		_capacity = capacity;
	}

	bool isEmpty() {
		return _size==0;
	}
	
	int size() {
		return _size;
	}
	
	int top() {
		return head ? head->data : -1;
	}
	
	void push(int element) {
		if(_size<_capacity) {
			ListNode *tmp = new ListNode(element);
			tmp->next = head;
			head = tmp;
			++_size;
		}
	}
	
	void pop() {
		if(head) head = head->next, --_size;
	}
};
```