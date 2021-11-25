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

bool is_bst(Node *n, int lower=INT_MIN, int upper=INT_MAX){
	if(!n) return true;
	return (
		n->value>lower && 
		n->value<upper && 
		is_bst(n->left, lower, n->value) &&
		is_bst(n->right, n->value, upper)
	);
}

signed main() {
	Node *n = new Node(5, new Node(3, new Node(1), new Node(4)), new Node(7, new Node(6)));
	cout << toBool(is_bst(n)) << endl;
	return 0;
}