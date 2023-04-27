#include <bits/stdc++.h>
#define toBool(x) (x ? "True" : "False")
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right;
	Node(int v, Node *l=NULL, Node *r=NULL)
		:value{v}, left{l}, right{r} {}
};

bool isValid(Node *tree, Node *subTree){
	if(tree and subTree) 
		return tree->value==subTree->value and 
		isValid(tree->left, subTree->left) and 
		isValid(tree->right, subTree->right);
	if(!tree and !subTree) return true;
	return false;
}

bool find_subtree(Node *tree, Node *subTree){
	if(tree && subTree){
		if(tree->value==subTree->value && isValid(tree, subTree))
			return true;
		return find_subtree(tree->left, subTree) or find_subtree(tree->right, subTree);
	}
	return tree==subTree;
}

signed main() {
	Node *tree = new Node(1, new Node(4, new Node(3), new Node(2)), new Node(5, new Node(4), new Node(-1)));
	Node *subTree = new Node(4, new Node(3), new Node(2));
	cout << toBool(find_subtree(tree, subTree)) << endl;
	return 0;
}