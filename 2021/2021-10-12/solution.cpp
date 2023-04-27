#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right;
	Node(int v, Node *l=NULL, Node *r=NULL)
		:value{v}, left{l}, right{r} {}
};

int min_depth_bt(Node *root) {
	if(!root) return 0;
	if(!root->left && !root->right) return 1;
	int ans = INT_MAX;
	if(root->left)
		ans = min(ans, min_depth_bt(root->left));
	if(root->right)
		ans = min(ans, min_depth_bt(root->right));
	return ans+1;
}

signed main() {
	Node *n = new Node(1, new Node(2), new Node(3, NULL, new Node(4)));
	/*
	      1
	     / \
	    2   3
	         \
	          4
	*/
	cout << min_depth_bt(n) << endl;

	n = new Node(1, 
		new Node(2, new Node(4)), 
		new Node(3, new Node(5, new Node(7), new Node(8)), new Node(6))
	);
	/*
	       1
	      / \
	     2   3
	    /   / \
	   4   5   6
	      / \
	     7   8
	*/
	cout << min_depth_bt(n);
	return 0;
}