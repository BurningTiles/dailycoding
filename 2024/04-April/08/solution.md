# Solution - 08 Apr 2024

---
## [1700. Number of Students Unable to Eat Lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch)

### cpp
```cpp
class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        int circular=0, square=0;
        
        for(int i=0; i<students.size(); ++i)
            students[i] ? ++square : ++circular;
        
        for(int i=0; i<sandwiches.size(); ++i) {
            sandwiches[i] ? --square : --circular;
            if(square < 0 || circular < 0) return students.size()-i;
        }
        
        return 0;
    }
};
```
