#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right;
	Node(int v, Node *l=NULL, Node *r=NULL)
		:value{v}, left{l}, right{r} {}
};

long long bst_numbers_sum(Node *root, long long cur=0){
	int ans=0;
	if(root){
		cur *= 10;
		cur += root->value;
		if(root->left || root->right){
			if(root->left)
				ans += bst_numbers_sum(root->left, cur);
			if(root->right)
				ans += bst_numbers_sum(root->right, cur);
		}
		else
			return cur;
	}
	return ans;
}

signed main() {
	Node *root = new Node(1, new Node(2, new Node(4), new Node(5)), new Node(3));
	
	cout << bst_numbers_sum(root);

	return 0;
}