# Solution - 30 May 2023

---
## [1. Implement Queue using Stacks](https://workat.tech/problem-solving/practice/implement-queue-using-stacks) [(LeetCode)](https://leetcode.com/problems/implement-queue-using-stacks/) 

```cpp
/* Use this Stack class
class Stack {
	Stack (int capacity)
	int size()
	boolean isEmpty()
	int top()
	void push(int element)
	void pop()
};
*/

// Implement the Queue class
class Queue {
	Stack *s1, *s2;
	int _capacity;
public:
	Queue (int capacity) {
		_capacity = capacity;
		s1 = new Stack(capacity);
		s2 = new Stack(capacity);
	}

	bool isEmpty() {
		return s1->isEmpty();
	}
	
	int size() {
		return s1->size();
	}
	
	int front() {
		return s1->top();
	}
	
	int back() {
		while(!s1->isEmpty())
			s2->push(s1->top()), s1->pop();
		int ans = s2->top();
		while(!s2->isEmpty())
			s1->push(s2->top()), s2->pop();
		return ans;
	}
	
	void push(int element) {
		if(s1->size()<_capacity){
			while(!s1->isEmpty())
				s2->push(s1->top()), s1->pop();
			s1->push(element);
			while(!s2->isEmpty())
				s1->push(s2->top()), s2->pop();
		}
	}
	
	void pop() {
		s1->pop();
	}
};
```

---
## [2. Implement Stack using Queues](https://workat.tech/problem-solving/practice/implement-stack-using-queues) [(LeetCode)](https://leetcode.com/problems/implement-stack-using-queues/) 

```cpp
/* Use this Queue class
class Queue {
	Queue (int capacity)
	int size()
	boolean isEmpty()
	int front()
	int back()
	void push(int element)
	void pop()
};
*/

// Implement the Stack class
class Stack {
	Queue *q;
	int _capacity;
public:
	
	Stack (int capacity) {
		q = new Queue(capacity);
		_capacity = capacity;
	}

	bool isEmpty() {
		return q->isEmpty();
	}
	
	int size() {
		return q->size();
	}
	
	int top() {
		return q->front();
	}
	
	void push(int element) {
		q->push(element);
		for(int i=1; i<q->size(); i++)
			q->push(q->front()), q->pop();
	}
	
	void pop() {
		q->pop();
	}
};
```