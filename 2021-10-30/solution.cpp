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
	Node *b = new Node(10, new Node(20), new Node(30, new Node(40), new Node(50)));

	Node *ans = findNode(a, b, a->right->left);
	ans ? cout << ans->value << endl : cout << "Null\n";

	return 0;
}