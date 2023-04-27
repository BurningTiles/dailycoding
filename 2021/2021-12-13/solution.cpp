#include <bits/stdc++.h>
using namespace std;

vector<string> findRestaurant(vector<string> l1, vector<string>l2){
	vector<string> ans;
	int least = INT_MAX, tmp;
	unordered_map<string , int> m1, m2;
	for(int i=0; i<l1.size(); i++) m1[l1[i]] = i+1;
	for(int i=0; i<l2.size(); i++) m2[l2[i]] = i+1;
	for(auto &str:l1){
		if(m2[str]){
			tmp = m1[str]+m2[str];
			if(tmp<least){
				least = tmp;
				ans.clear();
				ans.push_back(str);
			} else if(tmp==least)
				ans.push_back(str);
		}
	}
	return ans;
}

void print(vector<string> v){
	cout << "[";
	for(int i=0; i<v.size(); i++)
		cout << "\"" << v[i] << "\"" << (i==v.size()-1 ? "" : ", ");
	cout << "]\n";
}

signed main() {
	print(findRestaurant({"Shogun","Tapioca Express","Burger King","KFC"}, {"Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"}));
	print(findRestaurant({"Shogun","Tapioca Express","Burger King","KFC"}, {"KFC","Burger King","Tapioca Express","Shogun"}));
	return 0;
}