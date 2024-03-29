# Solution - 17 Dec 2023

---
## [2353. Design a Food Rating System](https://leetcode.com/problems/design-a-food-rating-system)

### cpp
```cpp
auto init = [](){ios::sync_with_stdio(0); cin.tie(0); cout.tie(0); return 0;}();

class FoodRatings {
    unordered_map<string, set<pair<int, string>>> cr; // cuisine ratings
    unordered_map<string, int> fr; // food ratings
    unordered_map<string, string> fc; // food cuisine

public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        for(int i=0; i<foods.size(); i++) {
            fr[foods[i]] = ratings[i];
            fc[foods[i]] = cuisines[i];
            cr[cuisines[i]].insert({ -ratings[i], foods[i] });
        }
    }
    
    void changeRating(string food, int newRating) {
        string c = fc[food];
        cr[c].erase({ -fr[food], food });
        cr[c].insert({ -newRating, food });
        fr[food] = newRating;
    }
    
    string highestRated(string cuisine) {
        return cr[cuisine].begin()->second;
    }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */
```
