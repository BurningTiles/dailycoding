# Solution - 27 Sep 2024

---
## [731. My Calendar II](https://leetcode.com/problems/my-calendar-ii)

### cpp
```cpp
class MyCalendarTwo {
    map<int, int> events;
public:
    MyCalendarTwo() { }
    
    bool book(int start, int end) {
        events[start]++;
        events[end]--;
        int booked = 0;

        for(auto e:events) {
            booked += e.second;
            if(booked > 2) {
                events[start]--;
                events[end]++;
                return false;
            }
        }

        return true;
    }
};

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo* obj = new MyCalendarTwo();
 * bool param_1 = obj->book(start,end);
 */
```
