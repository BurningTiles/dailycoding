#include <bits/stdc++.h>
using namespace std;

class Node{
	public:
	int value;
	Node *next;
	Node(int v, Node *n=NULL)
		:value{v}, next{n}{}
};

Node* rotate_list(Node *n, int k){
	if(k==0 || !n) return n;
	int i=1;
	Node *tmp=n, *ans = NULL;
	while(i<k && tmp->next)
		++i, tmp=tmp->next;
	if(!tmp->next && i<=k)
		return rotate_list(n, k%i);
	ans = tmp->next;
	tmp->next = NULL;
	tmp = ans;
	while(tmp->next)
		tmp=tmp->next;
	tmp->next=n;
	return ans;
}

void print(Node *n){
	while(n){
		cout << n->value << " ";
		n = n->next;
	} cout << endl;
}

signed main() {
	Node *n = new Node(1, new Node(2, new Node(3, new Node(4, new Node(5)))));
	print(rotate_list(n, 2));
	return 0;
}