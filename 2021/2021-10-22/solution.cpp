#include <bits/stdc++.h>
using namespace std;

class LRUCache{
	int size;
	list<pair<int, int>> pages;
	unordered_map<int, list<pair<int, int>>::iterator> pages_map;
	public:
	LRUCache(int s){
		size = s>0 ? s : 0;
	}

	void put(int key, int value){
		if(pages_map.find(key) == pages_map.end()){
			if(pages.size()==size){
				pages_map.erase(pages.back().first);
				pages.pop_back();
			}
			pages.push_front({key, value});
			pages_map[key] = pages.begin();
		}
		else {
			pages.erase(pages_map[key]);
			pages.push_front({key, value});
			pages_map[key] = pages.begin();
		}
	}

	int get(int key){
		int value = -1;
		if(pages_map.find(key) != pages_map.end()){
			value = pages_map[key]->second;
			pages.erase(pages_map[key]);
			pages.push_front({key, value});
			pages_map[key] = pages.begin();
		}
		return value;
	}
};

void print(int n){
	n==-1? cout << "None" : cout << n;
	cout << endl;
}

signed main(){
	LRUCache cache(2);
	cache.put(3, 3);
	cache.put(4, 4);
	print(cache.get(3));
	print(cache.get(2));
	cache.put(2, 2);
	print(cache.get(4));
	print(cache.get(3));

	return 0;
}