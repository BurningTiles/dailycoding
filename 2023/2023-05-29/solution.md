# Solution - 29 May 2023

---
## [1. Implement Queue using Array](https://workat.tech/problem-solving/practice/implement-queue-array) 

```cpp
// Implement the Queue class
class Queue {
	int *data, f=0, r=-1, _size=0, _capacity;
public:
	
	Queue (int capacity) {
		_capacity = capacity;
		data = new int[capacity];
	}

	bool isEmpty() {
		return _size == 0;
	}
	
	int size() {
		return _size;
	}
	
	int front() {
		return isEmpty() ? -1 : data[f];
	}
	
	int back() {
		return isEmpty() ? -1 : data[r];
	}
	
	void push(int element) {
		if(_size<_capacity) {
			r = (r+1) % _capacity;
			data[r] = element;
			++_size;
		}
	}
	
	void pop() {
		if(_size) {
			f = (f+1) % _capacity;
			--_size;
		}
	}
};
```

---
## [2. Implement Queue using Linked List](https://workat.tech/problem-solving/practice/implement-queue-linked-list) 

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

// Implement the Queue class
class Queue {
	ListNode *head, *tail;
	int _size, _capacity;
public:
	Queue (int capacity) {
		head = tail = NULL;
		_size = 0;
		_capacity = capacity;
	}

	bool isEmpty() {
		return _size == 0;
	}
	
	int size() {
		return _size;
	}
	
	int front() {
		return head ? head->data : -1;
	}
	
	int back() {
		return tail ? tail->data : -1;
	}
	
	void push(int element) {
		if(_size<_capacity) {
			ListNode *tmp = new ListNode(element);
			++_size;
			if(!head)
				head = tail = tmp;
			else
				tail->next = tmp, tail = tmp;
		}
	}
	
	void pop() {
		if(_size) {
			head = head->next, --_size;
			if(!head) tail = head;
		}
	}
};
```