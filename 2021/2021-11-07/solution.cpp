#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int value;
	Node *next;
	Node(int v=0, Node *n=NULL)
		:value{v}, next{n} {}
	string toStr(){
		if(next)
			return to_string(value) + " " + next->toStr();
		return to_string(value);
	}
};

Node* deleteDuplicates(Node *n){
	Node *ans = new Node(-1, n);
	Node *prev = ans, *cur = n;
	while(cur){
		while(cur->next && prev->next->value == cur->next->value)
			cur = cur->next;
		if(prev->next == cur)
			prev = prev->next;
		else
			prev->next = cur->next;
		cur = cur->next;
	}
	return ans->next;
}

signed main() {
	Node *n = new Node(1, new Node(2, new Node(3, new Node(3, new Node(4)))));
	n = deleteDuplicates(n);
	cout << (n ? n->toStr() : "Null") << endl;
	
	return 0;
}