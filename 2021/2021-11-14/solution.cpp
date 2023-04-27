#include <bits/stdc++.h>
#define toBool(x) (x ? "true" : "false")
using namespace std;

class Node{
	public:
	char value;
	Node *next, *prev;
	Node(char v, Node *n=NULL, Node *p=NULL)
		:value{v}, next{n}, prev{p} {}
};

bool is_palindrome(Node *n){
	Node *l=n, *r=n;
	while(r->next) r=r->next;
	while(l->next){
		if(l->value!=r->value) return false;
		l = l->next;
		r = r->prev;
	}
	return true;
}

signed main() {
	Node *n = new Node('a', new Node('b'));
	n->next->prev = n;
	n->next->next = new Node('b');
	n->next->next->prev = n->next;
	n->next->next->next = new Node('a');
	n->next->next->next->prev = n->next->next;

	cout << toBool(is_palindrome(n));

	return 0;
}