
# 26 Sep 2023

# Questions

---
## [1. Rod Cutting](https://workat.tech/problem-solving/practice/rod-cutting) 

<p>You are given a rod of length <code>n</code>, and an array <code>prices</code> of size <code>n</code> which contains the prices of rods of lengths 1 to n. Find the maximum amount you can make if you cut up the rod optimally.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>n: 8
A: [1, 3, 4, 5, 7, 9, 10, 11]
Result: 12
Explanation: Rods of length 2 and 6 cost: 3 + 9</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.<br/>
For each test case, the input has two lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the length of the rod.</li>
<li><em>n</em> space-separated integers denoting the price of rods.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with one integer denoting the maximum amount possible.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
8
1 3 4 5 7 9 10 11
6
3 5 8 10 14 15
7
2 8 11 14 15 19 21</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>12
18
27</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 5000</code><br/>
<code>1 &lt;= prices<sub>i</sub> &lt;= 10<sup>6</sup></code><br/>
<code>1 &lt;= answer &lt;= 10<sup>9</sup></code></p>

---
# [Solution](solution.md)
