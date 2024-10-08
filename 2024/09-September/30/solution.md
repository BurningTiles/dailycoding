# Solution - 30 Sep 2024

---
## [1381. Design a Stack With Increment Operation](https://leetcode.com/problems/design-a-stack-with-increment-operation)

### cpp
```cpp
class CustomStack {
    int *arr, limit=0, top = 0;
public:
    CustomStack(int maxSize) {
        arr = new int[maxSize];
        limit = maxSize;
    }
    
    void push(int x) {
        if(top<limit)
            arr[top++] = x;
    }
    
    int pop() {
        if(top>0)
            return arr[--top];
        return -1;
    }
    
    void increment(int k, int val) {
        for(int i=0; i<k && i<top; ++i)
            arr[i] += val;
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */
```
