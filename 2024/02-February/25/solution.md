# Solution - 25 Feb 2024

---
## [2709. Greatest Common Divisor Traversal](https://leetcode.com/problems/greatest-common-divisor-traversal)

### cpp
```cpp
class Graph {
    int n;
    vector<int> parent, compSize;

    int getParent(int x) {
        if(parent[x] == x) return x;
        return parent[x] = getParent(parent[x]);
    }

    void unionSet(int x, int y) {
        int px = getParent(x), py = getParent(y);
        if (px != py) {
            if(compSize[px] < compSize[py])
                swap(px, py);
            parent[py] = px;
            compSize[px] += compSize[py];
        }
    }

public:
    Graph(int n=0): n(n) {
        parent.resize(n);
        compSize.resize(n, 1);
        iota(parent.begin(), parent.end(), 0);
    }

    void addEdge(int x, int y) {
        unionSet(x, y);
    }

    bool isConnected() {
        return compSize[getParent(0)] == n;
    }
};

class Solution {
    vector<int> getPrimeFactors(int x) {
        vector<int> primeFactors;
        for(int i=2; i*i <=x; ++i) {
            if (x % i == 0) {
                primeFactors.push_back(i);
                while(x % i == 0)
                    x /= i;
            }
        }

        if(x != 1) 
            primeFactors.push_back(x);
        
        return primeFactors;
    }

public:
    bool canTraverseAllPairs(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return true;
        Graph g(n);
        unordered_map<int, int> used;
        
        for(int i=0; i<n; ++i) {
            if(nums[i] == 1) return false;

            vector<int> primeFactors = getPrimeFactors(nums[i]);
            for(int prime:primeFactors) {
                if(used.find(prime) != used.end())
                    g.addEdge(i, used[prime]);
                else
                    used[prime] = i;
            }
        }

        return g.isConnected();
    }
};
```
