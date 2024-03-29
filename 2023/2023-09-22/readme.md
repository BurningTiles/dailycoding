
# 22 Sep 2023

# Questions

---
## [1. Subset Sum 2](https://workat.tech/problem-solving/practice/subset-sum-2) 

<p>Given a set <code>A</code> composed of non-negative integers, find if it has a subset with sum equal to a given <code>target</code>.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>A: [3, 0, 4, 9, 5]
target: 17
Result: True
Explanation: The subset [3, 9, 5] has a sum of 17</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.<br/>
For each test case, the input has two lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the length of the array A.</li>
<li><em>n</em> space-separated integers denoting the elements of the array A.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with one integer denoting if any subset has sum target - 1 if true, 0 if false.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
5 17
3 0 4 9 5
5 20
3 0 4 9 5
5 16
2 2 5 4 8
1 2
1</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1
0
1
0</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 100</code><br/>
<code>1 &lt;= target &lt;= 10000</code><br/>
<code>0 &lt;= A<sub>i</sub> &lt;= 10000</code></p>

---
# [Solution](solution.md)
