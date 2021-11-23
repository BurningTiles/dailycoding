# Determine If Linked List is Palindrome

### Python
```python
class Node():
	def __init__(self, value, next=None, prev=None):
		self.value = value
		self.next = next
		self.prev = prev

def is_palindrome(n):
	l, r = n, n
	while r.next!=None:
		r = r.next
	while l.next!=None:
		if l.value!=r.value:
			return False
		l = l.next
		r = r.prev
	return True

node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('b')
node.next.next.prev = node.next
node.next.next.next = Node('a')
node.next.next.next.prev = node.next.next

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
	Node *next, *prev;
	Node(char v, Node *n=NULL, Node *p=NULL)
		:value{v}, next{n}, prev{p} {}
};

bool is_palindrome(Node *n){
	Node *l=n, *r=n;
	while(r->next) r=r->next;
	while(l->next){
		if(l->value!=r->value) return false;
		l = l->next;
		r = r->prev;
	}
	return true;
}

signed main() {
	Node *n = new Node('a', new Node('b'));
	n->next->prev = n;
	n->next->next = new Node('b');
	n->next->next->prev = n->next;
	n->next->next->next = new Node('a');
	n->next->next->next->prev = n->next->next;

	cout << toBool(is_palindrome(n));

	return 0;
}
```