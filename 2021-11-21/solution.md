# Determine If Singly Linked List is Palindrome

### Python
```python
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def is_palindrome(node):
	s=[]
	p1, p2 = node, node
	while p2!=None and p2.next!=None:
		s.append(p1.value)
		p1 = p1.next
		p2 = p2.next.next
	if p2!=None:
		p1 = p1.next
	
	while len(s)>0:
		if s[-1]!=p1.value: return False
		p1 = p1.next
		del s[-1]
	return True

node = Node('a', Node('b', Node('b', Node('a'))))
print(is_palindrome(node))
```

### C++
```cpp
#include <bits/stdc++.h>
#define toBool(x) (x ? "true" : "false")
using namespace std;

class Node{
	public:
	char value;
	Node *next;
	Node(char v, Node *n=NULL)
		:value{v}, next{n}{}
};

bool is_palindrome(Node *n){
	stack<char> stk;
	Node *p1 = n, *p2 = n;
	while(p2 && p2->next){
		stk.push(p1->value);
		p1 = p1->next;
		p2 = p2->next->next;
	}
	if(p2) p1 = p1->next;

	while(stk.size()){
		if(stk.top()!=p1->value) return false;
		p1 = p1->next;
		stk.pop();
	}
	return true;
}

signed main() {
	Node *n = new Node('a', new Node('b', new Node('b', new Node('a'))));
	cout << toBool(is_palindrome(n)) << endl;
	return 0;
}
```