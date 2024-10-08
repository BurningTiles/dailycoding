# Solution - 28 Sep 2024

---
## [641. Design Circular Deque](https://leetcode.com/problems/design-circular-deque)

### cpp
```cpp
class MyCircularDeque {
    int *v, size, limit, front, rear;
public:
    MyCircularDeque(int k) {
        v = new int[k];
        limit = k;
        size = 0;
        front = rear = -1;
    }
    
    bool insertFront(int value) {
        if(size == limit) return false;
        if(front == -1) {
            front = rear = 0;
            v[front] = value;
        } else {
            front = (front+1) % limit;
            v[front] = value;
        }
        ++size;
        return true;
    }
    
    bool insertLast(int value) {
        if(size == limit) return false;
        if(rear == -1) {
            front = rear = 0;
            v[0] = value;
        } else {
            rear = (rear - 1 + limit) % limit;
            v[rear] = value;
        }
        ++size;
        return true;
    }
    
    bool deleteFront() {
        if(size == 0) return false;
        if(--size == 0) front = rear = -1;
        else
            front = (front - 1 + limit) % limit;
        return true;
    }
    
    bool deleteLast() {
        if(size == 0) return false;
        if(--size == 0) front = rear = -1;
        else
            rear = (rear + 1) % limit;
        return true;
    }
    
    int getFront() {
        if(size == 0) return -1;
        return v[front];
    }
    
    int getRear() {
        if(size == 0) return -1;
        return v[rear];
    }
    
    bool isEmpty() {
        return size == 0;
    }
    
    bool isFull() {
        return limit == size;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */
```
