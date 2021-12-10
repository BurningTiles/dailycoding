#include <bits/stdc++.h>
#define i2d vector<vector<int>>
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right;
	Node(int v, Node *l=NULL, Node *r=NULL)
		:value{v}, left{l}, right{r} {}
	void print(){
		cout << value << " ";
		if(left) left->print(); if(right) right->print();
	};
};

string serialize(Node *n){
	if(!n) return "# ";
	return to_string(n->value) + " " + serialize(n->left) + serialize(n->right);
}
Node* deserialize_rec(string &s){
	if(!s.size() || s[0]=='#') {
		if(s.size()<2) s="";
		else s = s.substr(2);
		return NULL;
	}
	Node *n = new Node(stoi(s));
	s = s.substr(s.find(" ")+1);
	n->left = deserialize_rec(s);
	n->right = deserialize_rec(s);
	return n;
}

Node* deserialize(string s){
	return deserialize_rec(s);
}

signed main() {
	Node *n = new Node(1, new Node(3, new Node(2), new Node(5)), new Node(4, NULL, new Node(7)));

	cout << serialize(n) << endl;
	deserialize("1 3 2 # # 5 # # 4 # 7 # #")->print();

	return 0;
}