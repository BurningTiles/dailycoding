#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right;
	Node(int v, Node *l=NULL, Node *r=NULL)
		:value{v}, left{l}, right{r} {}
};

int maxAncestorDiff(Node *n, int mn=INT_MAX, int mx=INT_MIN){
	if(!n) return mx-mn;
	mn = min(mn, n->value), mx = max(mx, n->value);
	return max(maxAncestorDiff(n->left, mn, mx), maxAncestorDiff(n->right, mn, mx));
}

signed main() {
	Node *n = new Node(8, new Node(3, new Node(1), new Node(6, new Node(4), new Node(7))), new Node(10, NULL, new Node(14, new Node(13))));
	cout << maxAncestorDiff(n) << endl;
	return 0;
}