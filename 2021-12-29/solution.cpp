#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right, *next;
	Node(int v, Node *l=NULL, Node *r=NULL, Node *n=NULL)
		:value{v}, left{l}, right{r}, next{n} {}
};

void connect(Node *root){
	Node *prev=root, *cur;
	while(prev){
		cur = prev;
		while(cur and cur->left){
			cur->left->next = cur->right;
			if(cur->next) cur->right->next = cur->next->left;
			cur = cur->next;
		}
		prev = prev->left;
	}
}

void print(Node *n){
	Node *cur, *next=n;
	while(next) {
		cur = next, next = cur->left;
		while(cur)
			cout << cur->value << " ", cur = cur->next;
		cout << "# ";
	}
	cout << endl;
}

signed main() {
	Node *n = new Node(1, new Node(2, new Node(4), new Node(5)), new Node(3, new Node(6), new Node(7)));
	connect(n);
	print(n);
	return 0;
}