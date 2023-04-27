#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right, *parent;
	Node(int v, Node *l=NULL, Node *r=NULL, Node *p=NULL)
		:value{v}, left{l}, right{r}, parent{p} {}
};

Node* inorder_successor(Node *n){
	Node *ans=NULL;
	if(n->right){
		ans = n->right;
		while(ans->left) ans = ans->left;
	}
	else if(n->parent){
		ans = n->parent;
		while(ans->parent && ans->value<n->value) ans = ans->parent;
		if(ans->value<n->value) ans = NULL;
	}
	return ans;
}

signed main() {
	Node *tree = new Node(3, new Node(2, new Node(1)), new Node(4, NULL, new Node(5))), *ans;
	tree->left->parent = tree;
	tree->right->parent = tree;
	tree->left->left->parent = tree->left;
	tree->right->right->parent = tree->right;

	ans = inorder_successor(tree->left);
	ans ? cout << ans->value << endl : cout << "NULL\n";

	ans = inorder_successor(tree->right);
	ans ? cout << ans->value << endl : cout << "NULL\n";
	return 0;
}