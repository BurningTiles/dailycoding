
# 21 Sep 2023

# Questions

---
## [1. Collect Jewels](https://workat.tech/problem-solving/practice/collect-jewels) 

<p>You discover a treasure containing <code>n</code> pieces of jewel stones. You have a sack to collect them but it can hold only contents upto weight <code>capacity</code>.</p>
<p>You are given the weight and value of each of the stones - <code>weight<sub>i</sub></code> and <code>value<sub>i</sub></code>.</p>
<p>Find the maximum value of stones that you can carry in the sack.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>stones(weight, value): [(1, 3), (2, 4), (3, 5), (4, 7)]
capacity: 5
Max value: 10
Explanation: Choose stones at index 0 and 3.</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.<br/>
For each test case, the input has the following lines:</p>
<ul>
<li>The first line contains two space-separated integers &lsquo;n&rsquo; and &lsquo;capacity&rsquo;.</li>
<li>The next <i>n</i> lines contains two space-separated integers - weight<sub>i</sub> and value<sub>i</sub>.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with one integer denoting the maximum value of stones that you can carry in the sack.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
4 5
1 3
2 4
3 5
4 7
5 25
2 4
6 14
5 13
9 21
8 18</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>10
57</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>3</sup></code><br/>
<code>1 &lt;= capacity &lt;= 5*10<sup>3</sup></code><br/>
<code>1 &lt;= weight<sub>i</sub> &lt;= 10<sup>3</sup></code><br/>
<code>1 &lt;= value<sub>i</sub> &lt;= 10<sup>3</sup></code></p>

---
# [Solution](solution.md)
