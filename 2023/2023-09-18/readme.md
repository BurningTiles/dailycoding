
# 18 Sep 2023

# Questions

---
## [1. Maximum Sum Increasing Subsequence](https://workat.tech/problem-solving/practice/maximum-sum-increasing-subsequence) 

<p>A maximum sum subsequence of an array is subsequence whose sum is maximum with the condition that the subsequence is sorted.</p>
<p>Given an array, find the sum of the maximum sum subsequence of that array.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>arr: [101, 4, 98, 103]
answer: 205
Explanation: 4+98+103</code></pre>
<pre class="plaintext hljs"><code>arr: [101, 4, 95, 103]
answer: 204
Explanation: 101+103</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.<br/>
For each test case, the input has two lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the size of the array.</li>
<li><em>n</em> space-separated integers denoting the array.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with one integer denoting the sum of the max sum subsequence.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
4
101 4 98 103
4
101 4 95 103
1
42</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>205
204
42</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n &lt;= 100</code><br/>
<code>1 &lt;= arr<sub>i</sub> &lt;= 1000</code></p>

---
# [Solution](solution.md)
