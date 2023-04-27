#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right;
	Node(int v, Node *l=NULL, Node *r=NULL)
		:value{v}, left{l}, right{r} {}
};

void bfs(Node *n, vector<Node*> &ans){
	if(!n) return;
	ans.push_back(n);
	bfs(n->left, ans);
	bfs(n->right, ans);
}

void flatten_bst(Node *n){
	if(!n) return;
	vector<Node*> v;
	bfs(n, v);
	v.push_back(NULL);
	for(int i=0; i<v.size()-1; i++)
		v[i]->left = NULL,
		v[i]->right = v[i+1];
}

void print(Node *n){
	if(!n) {
		cout << "None";
		return;
	}
	cout << "(" << n->value << ", ";
	print(n->left);
	cout << ", ";
	print(n->right);
	cout << ")";
}

signed main() {
	Node *n = new Node(1, new Node(2, new Node(5)), new Node(3, new Node(4)));
	
	flatten_bst(n);
	print(n);
	return 0;
}