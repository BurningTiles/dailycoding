#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right;
	Node(int v, Node *l=NULL, Node *r=NULL)
		:value{v}, left{l}, right{r} {}
};

void node_to_vector(Node *root, vector<Node*> &v) {
	if(root){
		v.push_back(root);
		node_to_vector(root->left, v);
		node_to_vector(root->right, v);
	}
}

void flatten_bst(Node *root) {
	vector<Node *> v;
	node_to_vector(root, v);
	for(int i=0; i<v.size()-1; i++){
		v[i]->left = NULL;
		v[i]->right = v[i+1];
	}
	if(v.size())
		v.back()->left = v.back()->right = NULL;
}

void print(Node *n){
	if(n){
		cout << "(" << n->value << ", ";
		print(n->left);
		cout << ", ";
		print(n->right);
		cout << ")";
	}
	else
		cout << "null";
}

signed main() {
	Node *root = new Node(1, new Node(2, new Node(5)), new Node(3, new Node(4)));
	
	cout << "Before:\n";
	print(root);

	flatten_bst(root);

	cout << "\n\nAfter:\n";
	print(root);

	return 0;
}