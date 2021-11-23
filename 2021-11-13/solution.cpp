#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right;
	Node(int v, Node *l=NULL, Node *r=NULL)
		:value{v}, left{l}, right{r} {}
};

int sum_rec(Node *n, unordered_map<int, int> &m){
	if(!n) return 0;
	int ans = n->value + sum_rec(n->left, m) + sum_rec(n->right, m);
	m[ans]++;
	return ans;
}

vector<int> most_freq_subtree_sum(Node *n){
	unordered_map<int, int> m;
	sum_rec(n, m);
	vector<int> ans;
	int max_freq=0;
	for(auto x:m)
		if(x.second>max_freq)
			max_freq=x.second,
			ans={x.first};
		else if(x.second==max_freq)
			ans.push_back(x.first);
	return ans;
}

inline void print(vector<int> v){
	cout << "["; 
	for(int i=0; i<v.size(); i++) 
		cout << v[i] << (i==v.size()-1 ? "" : ", "); 
	cout << "]\n";
}

signed main() {
	Node *n = new Node(3, new Node(1), new Node(-3));
	print(most_freq_subtree_sum(n));

	n = new Node(5, new Node(2), new Node(-3));
	print(most_freq_subtree_sum(n));

	return 0;
}