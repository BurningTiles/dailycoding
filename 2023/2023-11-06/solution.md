# Solution - 06 Nov 2023

---
## [1845. Seat Reservation Manager](https://leetcode.com/problems/seat-reservation-manager)

### cpp
```cpp
class SeatManager {
    int end;
    set<int> blank;
public:
    SeatManager(int n) {
        end = 0;
    }
    
    int reserve() {
        int i = -1;
        if(blank.size()) {
            i = *blank.begin();
            blank.erase(*blank.begin());
        } else
            i = end++;
        return i+1;
    }
    
    void unreserve(int seatNumber) {
        blank.insert(seatNumber-1);
    }
};

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager* obj = new SeatManager(n);
 * int param_1 = obj->reserve();
 * obj->unreserve(seatNumber);
 */
```
