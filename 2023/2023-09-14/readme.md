
# 14 Sep 2023

# Questions

---
## [1. Longest Increasing Subsequence (LIS)](https://workat.tech/problem-solving/practice/longest-increasing-subsequence) [(LeetCode)](https://leetcode.com/problems/longest-increasing-subsequence/) 

<p>Given an array <code>A</code>, find the length of the longest strictly increasing subsequence (LIS).</p>
<p>A subsequence is a sequence that can be derived from an array by deleting some or no elements such that the order of the remaining elements remain the same.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>A: [10, 20, 2, 5, 3, 8, 8, 25, 6]
Result: 4
Explanation: Longest increasing subsequence: [2, 5, 8, 25]</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.<br/>
For each test case, the input has two lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the length of the array A.</li>
<li><em>n</em> space-separated integers denoting the elements of the array A.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with one integer denoting the length of the longest increasing subsequence.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>5
9
10 20 2 5 3 8 8 25 6
7
10 -63 7 -50 32 -9 -3
7
71 0 4 42 -31 4 -42
6
77 0 -2 25 1 70
7
2 2 1 5 7 -50 80</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>4
4
3
3
4</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 3000</code><br/>
<code>-10<sup>9</sup> &lt;= A<sub>i</sub> &lt;= 10<sup>9</sup></code></p>

---
# [Solution](solution.md)
