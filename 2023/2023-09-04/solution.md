# Solution - 04 Sep 2023

---
## [1. Serialize and Deserialize Binary Search Tree (BST)](https://workat.tech/problem-solving/practice/serialize-and-deserialize-bst) [(LeetCode)](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) 

### cpp
```cpp
/* This is the Node class definition

class Node {
public:
	Node* left;
	Node* right;
	int data;

	Node(int data) {
		this->left = NULL;
		this->right = NULL;
		this->data = data;
	}
};
*/

string serialize(Node* root) {
	if(!root) return "-1";
	return to_string(root->data) + " " + 
		serialize(root->left) + " " +
		serialize(root->right);
}

Node* deserialize(stringstream &ss) {
	int data; ss >> data;
	if(data == -1) return NULL;
	Node *n = new Node(data);
	n->left = deserialize(ss);
	n->right = deserialize(ss);
	return n;
}

Node* deserialize(string serializedTree) {
	stringstream ss(serializedTree);
	return deserialize(ss);
}

/*
// Without recursion
string serialize(Node* root) {
	queue<Node*> q;
	q.push(root);
	vector<int> v;
	while(q.size()) {
		Node *n = q.front(); q.pop();
		if(n){
			v.push_back(n->data);
			q.push(n->left);
			q.push(n->right);
		} else v.push_back(-1);
	}
	while(v.size() && v.back() == -1) v.pop_back();
	if(!v.size()) return "";
	string ans = to_string(v[0]);
	for(int i=1; i<v.size(); i++)
		ans += " " + to_string(v[i]);
	return ans;
}

Node* deserialize(string serializedTree) {
	stringstream ss(serializedTree);
	vector<Node*> v;
	int tmp;
	while((ss >> tmp))
		v.push_back(tmp != -1 ? new Node(tmp) : NULL);
	int n = v.size();
	if(!n) return NULL;
	for(int i=0, j=1; i<n; i++) {
		if(v[i]) {
			if(j<n) v[i]->left = v[j++];
			if(j<n) v[i]->right = v[j++];
		}
	}
	return v[0];
}
*/
```
