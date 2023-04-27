#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right;
	Node(int v, Node *l=NULL, Node *r=NULL)
		:value{v}, left{l}, right{r} {}
};

int maxPathDown(Node *n, int &mx){
	if(!n) return 0;
	int left = max(0, maxPathDown(n->left, mx));
	int right = max(0, maxPathDown(n->right, mx));
	mx = max(mx, left+right+n->value);
	return max(left, right)+n->value;
}

int maxPathSum(Node *n){
	int ans=INT_MIN;
	maxPathDown(n, ans);
	return ans;
}

signed main() {
	Node *n = new Node(10, new Node(2, new Node(20), new Node(1)), new Node(10, NULL, new Node(-25, new Node(3), new Node(4))));
	cout << maxPathSum(n) << endl;
	return 0;
}