# Solution - 26 Sep 2024

---
## [729. My Calendar I](https://leetcode.com/problems/my-calendar-i)

### cpp
```cpp
class MyCalendar {
    map<int, int> events;
public:
    MyCalendar() {}
    
    bool book(int start, int end) {
        auto next = events.upper_bound(start);
        if(next != events.end() && next->second < end) return false;
        events[end] = start;
        return true;
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */
```
