# Deep Copy Graph

### Python
```python
class Node:
	def __init__(self, value, adj=None):
		self.value = value
		self.adj = adj
		self._print_visited = set()
		if adj==None:
			self.adj = []
	
	def __repr__(self):
		if self in self._print_visited:
			return ""
		self._print_visited.add(self)
		ans = ""
		for n in self.adj:
			ans += f'{n}\n'
		self._print_visited.remove(self)
		return ans + f"({self.value}, {[n.value for n in self.adj]})"

def deep_copy_graph(n, visited={}):
	if n.value in visited:
		return visited[n.value]
	ans = Node(n.value)
	visited[n.value] = ans
	for x in n.adj:
		ans.adj.append(deep_copy_graph(x, visited))
	return ans

n5 = Node(5)
n4 = Node(4)
n3 = Node(3, [n4])
n2 = Node(2)
n1 = Node(1, [n5])
n5.adj = [n3]
n4.adj = [n3, n2]
n2.adj = [n4]

graph_copy = deep_copy_graph(n1)
print(graph_copy)
```

### C++
```cpp
#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int value;
	vector<Node*> adj;
	Node(int v, vector<Node*> a={})
		:value{v}, adj{a} {}
};

Node* deep_copy_graph(Node *n, unordered_map<int, Node*> visited={}){
	if(visited[n->value]!=NULL)
		return visited[n->value];
	Node *ans = new Node(n->value);
	visited[n->value] = ans;
	for(int i=0; i<n->adj.size(); i++)
		ans->adj.push_back(deep_copy_graph(n->adj[i], visited));
	return ans;
}

void print(Node *n, unordered_map<int, bool> visited={}){
	if(visited[n->value]) return;
	visited[n->value] = true;
	int size = n->adj.size();
	for(int i=0; i<size; i++)
		print(n->adj[i], visited);
	cout << "(" << n->value << ", [";
	for(int i=0; i<size; i++)
		cout << n->adj[i]->value << (i==size-1 ? "" : ", ");
	cout << "])" << endl;
}

signed main() {
	Node *n5 = new Node(5), 
	     *n4 = new Node(4), 
		 *n3 = new Node(3, {n4}),
		 *n2 = new Node(2),
		 *n1 = new Node(1, {n5});
	n5->adj = {n3};
	n4->adj = {n3, n2};
	n2->adj = {n4};
	
	Node *ans = deep_copy_graph(n1);
	print(ans);

	return 0;
}
```