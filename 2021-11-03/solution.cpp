#include <bits/stdc++.h>
#define toBool(x) (x ? "true" : "false")
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right;
	Node(int v, Node *l=NULL, Node *r=NULL)
		:value{v}, left{l}, right{r} {}
};

void getLeafs(Node *n, vector<int> &v){
	if(!n) return;
	if(!n->left && !n->right)
		v.push_back(n->value);
	if(n->left)
		getLeafs(n->left, v);
	if(n->right)
		getLeafs(n->right, v);
}

bool leafSimilar(Node *n1, Node *n2){
	vector<int> v1, v2;
	getLeafs(n1, v1);
	getLeafs(n2, v2);
	if(v1.size() == v2.size()){
		for(int i=0; i<v1.size(); i++)
			if(v1[i]!=v2[i]) return false;
		return true;
	}
	return false;
}

signed main() {
	Node *n1 = new Node(3, new Node(5, new Node(6), new Node(2)), new Node(1));
	Node *n2 = new Node(7, new Node(2, new Node(6), new Node(2)), new Node(1));
	cout << toBool(leafSimilar(n1, n2)) << endl;
	return 0;
}