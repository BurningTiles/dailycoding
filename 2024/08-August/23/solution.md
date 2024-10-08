# Solution - 23 Aug 2024

---
## [592. Fraction Addition and Subtraction](https://leetcode.com/problems/fraction-addition-and-subtraction)

### cpp
```cpp
class Solution {
public:
    string fractionAddition(string expression) {
        expression.push_back('+');
        long long numerator = 0, denominator = 2520, curNum = 0, cur = 0, tmp;
        bool minus = false, denom = false;

        for (auto ch : expression) {
            if (ch == '-' || ch == '+') {
                if (curNum || cur) {
                    if (denom)
                        tmp = curNum * (denominator / cur);
                    else
                        tmp = cur * denominator;

                    numerator += (minus ? -tmp : tmp);
                }
                cur = 0;
                minus = ch == '-';
                denom = false;
            } else if (ch == '/') {
                curNum = cur;
                cur = 0;
                denom = true;
            } else
                cur = cur * 10 + ch - '0';
        }

        for (int i = 10; i > 1; --i) {
            while (numerator % i == 0 && denominator % i == 0)
                numerator /= i, denominator /= i;
        }

        return to_string(numerator) + "/" + to_string(denominator);
    }

    /*
    // Another solution using builtin functions;
    string fractionAddition(string expression) {
        istringstream iss(expression);
        int numerator = 0, denominator = 1, a, b;
        char ch;

        while (iss >> a >> ch >> b) {
            numerator = numerator * b + a * denominator;
            denominator *= b;
            const int common = abs(__gcd(numerator, denominator));
            numerator /= common;
            denominator /= common;
        }
        return to_string(numerator) + "/" + to_string(denominator);
    }
    */
};
```
