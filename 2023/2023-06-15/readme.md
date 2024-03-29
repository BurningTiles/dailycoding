
# 15 Jun 2023

# Questions

---
## [1. Count Set Bits](https://workat.tech/problem-solving/practice/count-set-bits) 

<p>Given a positive integer <code>n</code>, count the number of set bits in the binary representation of <code>n</code>.</p>
<table>
    <thead>
        <tr><td style="width:100px">n</td><td style="width:100px">Binary(n)</td><td style="width:100px"># Set Bits</td></tr>
    <thead>
    <tbody>
        <tr><td>1</td><td>1</td><td>1</td></tr>
        <tr><td>5</td><td>101</td><td>2</td></tr>
        <tr><td>8</td><td>1000</td><td>1</td></tr>
    </tbody>
</table>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.</p>
<p>For each test case, the input has one line containing a positive integer &lsquo;n&rsquo;.</p>
<h4>Output Format</h4>
<p>For each test case, the output has one line containing the number of set bits in the binary representation of n.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
1
5
8</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1
2
1</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10<sup>5</sup></code><br/>
<code>1 &lt;= n &lt;= 10<sup>9</sup></code></p>

---
## [2. Find the Duplicate Number](https://workat.tech/problem-solving/practice/find-the-duplicate-number) 

<p>You are given a list of integers <code>nums</code> of size <code>n+1</code>. Each number in <code>nums</code> lies from <code>1</code> to <code>n</code>.<br/>
All numbers appear once, except <code>x</code> which appears twice.</p>
<p>Find the number <code>x</code>.</p>
<h5>Example 1</h5>
<pre class="plaintext hljs"><code><strong>nums:</strong> [3, 1, 2, 4, 2]
<strong>Answer:</strong> 2</code></pre>
<h5>Example 2</h5>
<pre class="plaintext hljs"><code><strong>nums:</strong> [3, 1, 3, 2]
<strong>Answer:</strong> 3</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.</p>
<p>For each test case, the input has two lines:</p>
<ul>
<li>The first line has a positive integer &lsquo;n&rsquo;.</li>
<li>The second line has <i>n+1</i> space-separated integers denoting the list <i>nums</i>.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has one line containing the value of x.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
4
3 1 2 4 2
3
3 1 3 2</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>2
3</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n &lt;= 10000</code></p>

---
# [Solution](solution.md)
