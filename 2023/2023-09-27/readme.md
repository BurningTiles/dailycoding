
# 27 Sep 2023

# Questions

---
## [1. Coin Change](https://workat.tech/problem-solving/practice/coin-change) 

<p>You are given coins of different denominations, represented by an array - <code>coins</code> of size <code>n</code>. You are also given a value - <code>target</code>. Find the different number of combinations that make up the amount <code>target</code>. Assume that you have infinite number of each kind of coin.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>coins: [5, 2, 4]
target: 13
Result: 3
Explanation: The three ways are-
2, 2, 2, 2, 5
2, 2, 4, 5
4, 4, 5</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.<br/>
For each test case, the input has two lines:</p>
<ul>
<li>Two space-separated integers &lsquo;n&rsquo; and &lsquo;target&rsquo;.</li>
<li><em>n</em> space-separated integers denoting the available denominations.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with one integer denoting the number of possible combinations.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
3 13
5 2 4
3 28
2 5 4
4 28
1 2 4 5</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>3
16
163</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 1000</code><br/>
<code>1 &lt;= target &lt;= 3000</code><br/>
<code>0 &lt;= C<sub>i</sub> &lt;= 2000</code><br/>
<code>0 &lt;= number of combinations &lt;= 10<sup>9</sup></code></p>

---
# [Solution](solution.md)
