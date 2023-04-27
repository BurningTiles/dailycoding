# Clone Trees

## Recursively
### Python
```python
class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def findNode(a, b, node):
	if a==None or b==None:
		return None
	if a == node:
		return b
	ans = findNode(a.left, b.left, node)
	return ans if ans!=None else findNode(a.right, b.right, node)

#   1
#  / \
# 2   3
#    / \
#   4*  5
a = Node(1, Node(2), Node(3, Node(4), Node(5)))

b = Node(1, Node(2), Node(3, Node(4), Node(5)))

print(findNode(a, b, a.right.left).value)
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right;
	Node(int v, Node *l=NULL, Node *r=NULL)
		:value{v}, left{l}, right{r} {}
};

Node* findNode(Node* a, Node* b, Node* node){
	if(!a || !b) return NULL;
	if(a == node) return b;
	Node *ans = findNode(a->left, b->left, node);
	return ans ? ans : findNode(a->right, b->right, node);
}

signed main() {
	/*
	 *    1
	 *   / \
	 *  2   3
	 *     / \
	 *    4*  5
	 */
	Node *a = new Node(1, new Node(2), new Node(3, new Node(4), new Node(5)));
	Node *b = new Node(1, new Node(2), new Node(3, new Node(4), new Node(5)));

	Node *ans = findNode(a, b, a->right->left);
	ans ? cout << ans->value << endl : cout << "Null\n";

	return 0;
}
```

## Iteratively
### Python
```python
class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def findNode(a, b, node):
	q = [a]
	q1 = [b]
	while q:
		tmp = q[0]
		tmp1 = q1[0]
		del q[0]
		del q1[0]
		if tmp==node:
			return tmp1
		if tmp.left!=None:
			q.append(tmp.left)
			q1.append(tmp1.left)
		if tmp.right!=None:
			q.append(tmp.right)
			q1.append(tmp1.right)
	return None

#   1
#  / \
# 2   3
#    / \
#   4*  5
a = Node(1, Node(2), Node(3, Node(4), Node(5)))

b = Node(1, Node(2), Node(3, Node(4), Node(5)))

print(findNode(a, b, a.right.left).value)
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right;
	Node(int v, Node *l=NULL, Node *r=NULL)
		:value{v}, left{l}, right{r} {}
};

Node* findNode(Node* a, Node* b, Node* node){
	queue<Node*> q;
	queue<Node*> q1;
	q.push(a);
	q1.push(b);
	Node *tmp, *tmp1;
	while(q.size()){
		tmp = q.front(), tmp1 = q1.front();
		q.pop(), q1.pop();
		if(tmp == node) return tmp1;
		if(tmp->left){
			q.push(tmp->left);
			q1.push(tmp1->left);
		}
		if(tmp->right){
			q.push(tmp->right);
			q1.push(tmp1->right);
		}
	}
	return NULL;
}

signed main() {
	/*
	 *    1
	 *   / \
	 *  2   3
	 *     / \
	 *    4   5
	 */
	Node *a = new Node(1, new Node(2), new Node(3, new Node(4), new Node(5)));
	Node *b = new Node(1, new Node(2), new Node(3, new Node(4), new Node(5)));

	Node *ans = findNode(a, b, a->right->left);
	ans ? cout << ans->value << endl : cout << "Null\n";

	return 0;
}
```