# Solution - 29 Jan 2024

---
## [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks)

### cpp
```cpp
class MyQueue {
    int data[100];
    int i=0, j=0;
public:
    MyQueue() {}
    
    void push(int x) {
        data[j++] = x;
    }
    
    int pop() {
        if(j>i) return data[i++];
        return -1;
    }
    
    int peek() {
        if(j>i) return data[i];
        return -1;
    }
    
    bool empty() {
        return j-i==0;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
```
