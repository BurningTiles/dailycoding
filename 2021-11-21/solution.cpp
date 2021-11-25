#include <bits/stdc++.h>
#define toBool(x) (x ? "true" : "false")
using namespace std;

class Node{
	public:
	char value;
	Node *next;
	Node(char v, Node *n=NULL)
		:value{v}, next{n}{}
};

bool is_palindrome(Node *n){
	stack<char> stk;
	Node *p1 = n, *p2 = n;
	while(p2 && p2->next){
		stk.push(p1->value);
		p1 = p1->next;
		p2 = p2->next->next;
	}
	if(p2) p1 = p1->next;

	while(stk.size()){
		if(stk.top()!=p1->value) return false;
		p1 = p1->next;
		stk.pop();
	}
	return true;
}

signed main() {
	Node *n = new Node('a', new Node('b', new Node('b', new Node('a'))));
	cout << toBool(is_palindrome(n)) << endl;
	return 0;
}