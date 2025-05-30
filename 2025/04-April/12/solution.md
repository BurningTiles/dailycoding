# Solution - 12 Apr 2025

---
## [3272. Find the Count of Good Integers](https://leetcode.com/problems/find-the-count-of-good-integers)

### cpp
```cpp
class Solution {
public:
    long long vectorToNum(const vector<int> &nums) {
        long long ans = 0;
        for(int n:nums) ans = ans * 10 + n;
        return ans;
    }

    long long fact(int num) {
        long long ans = 1;
        for(int i=2; i<=num; ++i) 
            ans *= i;
        return ans;
    }

    long long totalPermutations(map<int, int> &mp, int total) {
        long long ans = fact(total);
        for(auto &palVal: mp)
            ans /= fact(palVal.second);
        return ans;
    }

    long long permsWithZero(map<int, int> mp, int total) {
        if(mp[0] == 0) return 0;
        mp[0]--;
        return totalPermutations(mp, total - 1);
    }

    void genPal(vector<int> &palNum, int left, int right, int div, int total, 
        set<map<int, int>> &visited, long long &ans) {
        if(left > right) {
            long long palVal = vectorToNum(palNum);

            if(palVal % div == 0) {
                map<int, int> digitMap;
                for(long long i = palVal; i; i/=10)
                    digitMap[i%10]++;
                
                if(!visited.count(digitMap)) {
                    ans += totalPermutations(digitMap, total) - permsWithZero(digitMap, total);
                    visited.insert(digitMap);
                }
            }

            return;
        }
        for(int i = (left == 0 ? 1 : 0); i <= 9; ++i) {
            palNum[left] = palNum[right] = i;
            genPal(palNum, left + 1, right - 1, div, total, visited, ans);
        }
    }

    long long countGoodIntegers(int n, int k) {
        vector<int> palNum(n);
        set<map<int, int>> visited;
        long long ans = 0;

        genPal(palNum, 0, n-1, k, n, visited, ans);

        return ans;
    }

    /*
    // Directly use precomputed answers.
    long long countGoodIntegers(int n, int k) {
        vector<vector<long long>> vals = {
            {9, 9, 243, 252, 10935, 10944, 617463, 617472, 41457015, 41457024},
            {4, 4, 108, 172, 7400, 9064, 509248, 563392, 37728000, 39718144},
            {3, 3, 69, 84, 3573, 3744, 206217, 207840, 13726509, 13831104},
            {2, 2, 54, 98, 4208, 6992, 393948, 494818, 33175696, 37326452},
            {1, 1, 27, 52, 2231, 3256, 182335, 237112, 15814071, 19284856},
            {1, 1, 30, 58, 2468, 3109, 170176, 188945, 12476696, 13249798},
            {1, 1, 33, 76, 2665, 3044, 377610, 506388, 36789447, 40242031},
            {1, 1, 27, 52, 2231, 5221, 292692, 460048, 30771543, 35755906},
            {1, 1, 23, 28, 1191, 1248, 68739, 69280, 4623119, 4610368}
        };
        
        return vals[k - 1][n - 1];
    }
    */
};
```
