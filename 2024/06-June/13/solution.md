# Solution - 13 Jun 2024

---
## [2037. Minimum Number of Moves to Seat Everyone](https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone)

### cpp
```cpp
class Solution {
public:
    int minMovesToSeat(vector<int>& seats, vector<int>& students) {
       sort(seats.begin(), seats.end());
       sort(students.begin(), students.end());
        int moves = 0;
        for( int i=0; i<seats.size(); i++)
            moves += abs(seats[i] - students[i]);
        
        return moves;
    }
};
```
