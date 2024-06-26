# Solution - 03 May 2024

---
## [165. Compare Version Numbers](https://leetcode.com/problems/compare-version-numbers)

### javascript
```js
/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
var compareVersion = function (version1, version2) {
    let v1 = version1.split('.').map(x => parseInt(x)).reverse();
    let v2 = version2.split('.').map(x => parseInt(x)).reverse();

    while(v1.length && v2.length) {
        if(v1.at(-1) < v2.at(-1)) return -1;
        if(v1.at(-1) > v2.at(-1)) return 1;
        v1.pop(); v2.pop();
    }

    const a = parseInt(v1.join('')) || 0, b = parseInt(v2.join('')) || 0;
    return a < b ? -1 : a > b ? 1 : 0;
};
```
