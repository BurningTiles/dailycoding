#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right;
	Node(int v, Node *l=NULL, Node *r=NULL)
		:value{v}, left{l}, right{r} {}
};

void helper(Node *n, int &depth, int &ans, int cur_depth=0){
	if(n){
		if(cur_depth>depth){
			depth = cur_depth;
			ans = n->value;
		}
		helper(n->left, depth, ans, cur_depth+1);
		helper(n->right, depth, ans, cur_depth+1);
	}
}

int findLeftmost(Node *n){
	int ans=0, depth=-1;
	helper(n, depth, ans);
	return ans;
}

signed main() {
	Node *n = new Node(2, new Node(1), new Node(3));
	cout << findLeftmost(n) << endl; 

	n = new Node(1, new Node(2, new Node(4)), new Node(3, new Node(5, new Node(7)), new Node(6)));
	cout << findLeftmost(n) << endl;  

	return 0;
}