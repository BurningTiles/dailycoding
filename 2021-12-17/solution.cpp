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

vector<int> zigzag_order(Node *n){
	deque<Node*> dq;
	dq.push_back(n);
	vector<int> ans;
	bool rev = false;
	int s=0, e=1;
	Node *tmp;
	while(dq.size()){
		tmp = dq.front();
		dq.pop_front();
		ans.push_back(tmp->value);
		if(tmp->left) dq.push_back(tmp->left);
		if(tmp->right) dq.push_back(tmp->right);
		if(e==ans.size()){
			if(rev) reverse(ans.begin()+s, ans.end());
			rev = !rev;
			s=e, e=s+dq.size();
		}
	}
	return ans;
}

void print(vector<int> v){
	cout << "[";
	for(int i=0; i<v.size(); i++)
		cout << v[i] << (i==v.size()-1 ? "" : ", ");
	cout << "]";
}

signed main() {
	Node *n = new Node(1, new Node(2, new Node(4), new Node(5)), new Node(3, new Node(6), new Node(7)));
	print(zigzag_order(n));

	return 0;
}