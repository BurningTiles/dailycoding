# Solution - 16 Jan 2024

---
## [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1)

### cpp
```cpp
class RandomizedSet {
    unordered_map<int, int> index;
    vector<int> data;
public:
    RandomizedSet() {}
    
    bool insert(int val) {
        if(index.count(val)) return false;

        index[val] = data.size();
        data.push_back(val);

        return true;
    }
    
    bool remove(int val) {
        if(!index.count(val)) return false;
        
        int i=index[val];
        data[i] = data.back();
        index[data[i]] = i;
        data.pop_back();
        index.erase(val);

        return true;
    }
    
    int getRandom() {
        return data[rand() % data.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
```
