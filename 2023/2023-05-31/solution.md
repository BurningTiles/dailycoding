# Solution - 31 May 2023

---
## [1. Balanced Parentheses](https://workat.tech/problem-solving/practice/balanced-parentheses) [(LeetCode)](https://leetcode.com/problems/valid-parentheses/) 

```cpp
bool isBalancedParentheses(string str) {
	stack<char> stk;
	for(auto &ch: str) {
		if(ch=='(') stk.push(')');
		else if(ch=='{') stk.push('}');
		else if(ch=='[') stk.push(']');
		else {
			if(!stk.size() || stk.top()!=ch) return false;
			stk.pop();
		}
	}
	return stk.empty();
}
```

---
## [2. Implement Min Stack](https://workat.tech/problem-solving/practice/min-stack) [(LeetCode)](https://leetcode.com/problems/min-stack/) 

```cpp
// Implement the below class
class MinStack {
	stack<pair<int, int>> stk;
public:
	void push(int x) {
		stk.push({x, stk.empty() ? x : min(stk.top().second, x)});
	}
	void pop() {
		stk.pop();
	}
	int top() {
		return stk.top().first;
	}
	int getMin() {
		return stk.top().second;
	}
};

/*
	// MinStack class and its object will be used as given below:
	MinStack *minStack = new MinStack();
	minStack->push(42);
	int top = minStack->top();
	int min = minStack->getMin();
	minStack->pop();
*/
```