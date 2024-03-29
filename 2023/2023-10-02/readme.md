
# 02 Oct 2023

# Questions

---
## [1. Maximum Product Subarray](https://workat.tech/problem-solving/practice/max-product-subarray) [(LeetCode)](https://leetcode.com/problems/maximum-product-subarray) 

<p>Given an array <code>A</code> of integers, find a contiguous non-empty subarray within the array that has the largest product, and return the <code>product</code>.</p>
<p><strong>Note:</strong> The product fits in a 32-bit integer.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>A: [-1, 3, 2, -1, -2, 3, 0, -2]
Result: 36
Explanation: The subarray [3, 2, -1, -2, 3] has a product of 36.</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.<br/>
For each test case, the input has two lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the length of the array A.</li>
<li><em>n</em> space-separated integers denoting the elements of the array A.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with one integer denoting the maximum product possible.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
8
-1 3 2 -1 -2 3 0 -2
7
3 0 -1 -2 3 0 -2
9
1 2 3 4 5 0 0 -1 1
1
-2</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>36
6
120
-2</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>5</sup></code><br/>
<code>-10<sup>9</sup> &lt;= A<sub>i</sub> &lt;= 10<sup>9</sup></code></p>

---
# [Solution](solution.md)
