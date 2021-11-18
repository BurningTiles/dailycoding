#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right;
	Node(int v, Node *l=NULL, Node *r=NULL)
		:value{v}, left{l}, right{r} {}
};

void inorder(Node *n){
	if(n){
		inorder(n->left);
		cout << n->value << " ";
		inorder(n->right);
	}
}

void inorder_iterative(Node *n){
	vector<Node*> s; // stack
	Node *cur = n;
	while(cur || s.size()){
		while(cur){
			s.push_back(cur);
			cur = cur->left;
		}
		cur = s.back();
		s.pop_back();
		cout << cur->value << " ";
		cur = cur->right;
	}
}

signed main() {
	Node *n = new Node(12, new Node(6, new Node(2), new Node(3)), new Node(4, new Node(7), new Node(8)));
	inorder(n);
	cout << endl;
	inorder_iterative(n);
	return 0;
}