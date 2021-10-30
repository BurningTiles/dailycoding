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
	Node *b = new Node(10, new Node(20), new Node(30, new Node(40), new Node(50)));

	Node *ans = findNode(a, b, a->right->left);
	ans ? cout << ans->value << endl : cout << "Null\n";

	return 0;
}