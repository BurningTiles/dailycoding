# Solution - 04 Oct 2023

---
## [1. Design HashMap](https://leetcode.com/problems/design-hashmap) 

### cpp
```cpp
#define N 1461
class MyHashMap {
    vector<pair<int, int>> data[N];
public:
    MyHashMap() {}
    
    void put(int key, int value) {
        for(auto &e:data[key%N])
            if(e.first==key) {
                e.second = value;
                return;
            }
        data[key%N].push_back({key, value});
    }
    
    int get(int key) {
        for(auto &e:data[key%N])
            if(e.first==key)
                return e.second;
        return -1;
    }
    
    void remove(int key) {
        for(auto &e:data[key%N])
            if(e.first==key)
                e.second = -1;
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */
```
