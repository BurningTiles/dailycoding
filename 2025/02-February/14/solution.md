# Solution - 14 Feb 2025

---
## [1352. Product of the Last K Numbers](https://leetcode.com/problems/product-of-the-last-k-numbers)

### cpp
```cpp
class ProductOfNumbers {
    vector<long long> products;
public:
    ProductOfNumbers() {
        products = {1};
    }
    
    void add(int num) {
        if(num == 0)
            products = {1};
        else
            products.push_back(products.back() * num);
    }
    
    int getProduct(int k) {
        if(k > products.size()-1)
            return 0;
        return products.back() / products[products.size()-k-1];
    }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */
```
