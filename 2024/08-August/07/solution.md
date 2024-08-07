# Solution - 07 Aug 2024

---
## [273. Integer to English Words](https://leetcode.com/problems/integer-to-english-words)

### cpp
```cpp
class Solution {
public:
    string numToString(int n) {
        string ones[20] = {"",        "One",       "Two",      "Three",
                           "Four",    "Five",      "Six",      "Seven",
                           "Eight",   "Nine",      "Ten",      "Eleven",
                           "Twelve",  "Thirteen",  "Fourteen", "Fifteen",
                           "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
        string tens[10] = {"",      "",      "Twenty",  "Thirty", "Forty",
                           "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};

        if (n == 0) return "";
        if (n < 20) return " " + ones[n];
        if (n < 100) return " " + tens[n / 10] + numToString(n % 10);
        if (n < 1000) return numToString(n / 100) + " Hundred" + numToString(n % 100);
        if (n < 1000000) return numToString(n / 1000) + " Thousand" + numToString(n % 1000);
        if (n < 1000000000) return numToString(n / 1000000) + " Million" + numToString(n % 1000000);
        return numToString(n / 1000000000) + " Billion" + numToString(n % 1000000000);
    }

    string numberToWords(int n) {
        if (n == 0) return "Zero";
        return numToString(n).substr(1);
    }
};
```
