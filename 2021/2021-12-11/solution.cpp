#include <bits/stdc++.h>
#define i2d vector<vector<int>>
using namespace std;

class Node{
	public:
	int value;
	Node *left, *right;
	Node(int v, Node *l=NULL, Node *r=NULL)
		:value{v}, left{l}, right{r} {}
};

vector<Node*> generateTrees(int e, int s=1) {
	if(s>e) return {NULL};
	vector<Node*> ans;
	for(int i=s; i<=e; i++){
		vector<Node*> left = generateTrees(i-1, s);
		vector<Node*> right = generateTrees(e, i+1);
		for(auto &l:left)
			for(auto &r:right)
				ans.push_back(new Node(i, l, r));
	}
	return ans;
}

string get(Node *n){
	deque<Node*> dq;
	dq.push_back(n);
	string ans = "[";
	while(dq.size()){
		Node *tmp = dq.front();
		dq.pop_front();
		if(!tmp){
			ans += "NULL, ";
			continue;
		}
		ans += to_string(tmp->value) + ", ";
		if(!tmp->left && !tmp->right) continue;
		dq.push_back(tmp->left);
		dq.push_back(tmp->right);
	}
	if(ans.size()>1) {
		ans = ans.substr(0, ans.size()-2);
		if(ans.back()=='L') ans = ans.substr(0, ans.size()-6);
	}
	ans += "]";
	return ans;
}

signed main() {
	vector<Node*> v = generateTrees(3);
	for(auto n:v)
		cout << get(n) << endl;

	return 0;
}