# Remove duplicates from Linked List

### Python
```python
class Node(object):
	def __init__(self, val, next=None):
		self.val = val
		self.next = next
	def __str__(self):
		if not self.next:
			return str(self.val)
		return str(self.val) + " " + str(self.next)

def deleteDuplicates(node):
	ans = Node(-1, node)
	prev, cur = ans, node
	while cur!=None:
		while cur.next!=None and prev.next.val == cur.next.val:
			cur = cur.next
		if prev.next == cur:
			prev = prev.next
		else:
			prev.next = cur.next
		cur = cur.next
	return ans.next

n = Node(1, Node(2, Node(3, Node(3, Node(4)))))
print(n)
n = deleteDuplicates(n)
print(n)
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int value;
	Node *next;
	Node(int v=0, Node *n=NULL)
		:value{v}, next{n} {}
	string toStr(){
		if(next)
			return to_string(value) + " " + next->toStr();
		return to_string(value);
	}
};

Node* deleteDuplicates(Node *n){
	Node *ans = new Node(-1, n);
	Node *prev = ans, *cur = n;
	while(cur){
		while(cur->next && prev->next->value == cur->next->value)
			cur = cur->next;
		if(prev->next == cur)
			prev = prev->next;
		else
			prev->next = cur->next;
		cur = cur->next;
	}
	return ans->next;
}

signed main() {
	Node *n = new Node(1, new Node(2, new Node(3, new Node(3, new Node(4)))));
	n = deleteDuplicates(n);
	cout << (n ? n->toStr() : "Null") << endl;
	
	return 0;
}
```