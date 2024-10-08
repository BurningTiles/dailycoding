# Solution - 29 Sep 2024

---
## [432. All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure)

### cpp
```cpp
class AllOne {
    struct Bucket {int value; unordered_set<string> keys;};
    list<Bucket> buckets;
    unordered_map<string, list<Bucket>::iterator> bucketOfKey;
public:
    AllOne() {}
    
    void inc(string key) {
        if(!bucketOfKey.count(key))
            bucketOfKey[key] = buckets.insert(buckets.begin(), {0, {key}});
        
        auto bucket = bucketOfKey[key], next = bucket;
        next++;

        if(next == buckets.end() || next->value > bucket->value + 1)
            next = buckets.insert(next, {bucket->value + 1, {}});
        next->keys.insert(key);
        bucketOfKey[key] = next;

        bucket->keys.erase(key);
        if (bucket->keys.empty())
            buckets.erase(bucket);
    }
    
    void dec(string key) {
        if(!bucketOfKey.count(key))
            return;
        
        auto bucket = bucketOfKey[key], prev = bucket;
        prev--;
        bucketOfKey.erase(key);

        if(bucket->value > 1) {
            if (bucket == buckets.begin() || prev->value < bucket->value - 1)
                prev = buckets.insert(bucket, {bucket->value - 1, {}});
            prev->keys.insert(key);
            bucketOfKey[key] = prev;
        }

        bucket->keys.erase(key);
        if (bucket->keys.empty())
            buckets.erase(bucket);
    }
    
    string getMaxKey() {
        return buckets.empty() ? "" : *(buckets.rbegin()->keys.begin());
    }
    
    string getMinKey() {
        return buckets.empty() ? "" : *(buckets.begin()->keys.begin());
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */
```
