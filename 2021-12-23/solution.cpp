#include <bits/stdc++.h>
#define toBool(x) (x ? "true" : "false")
using namespace std;

bool has_character_map(string s1, string s2){
	if(s1.size() != s2.size()) return false;
	int map[128] = {0};
	for(int i=0; i<s1.size(); i++)
		if(!map[s1[i]] or map[s1[i]]==s2[i]) map[s1[i]]=s2[i];
		else return false;
	return true;
}

signed main() {
	cout << toBool(has_character_map("abc", "def")) << endl;
	cout << toBool(has_character_map("aac", "def")) << endl;
	return 0;
}