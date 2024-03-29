
# 28 Sep 2023

# Questions

---
## [1. Decode Ways](https://workat.tech/problem-solving/practice/decode-ways) 

<p>A message containing letters from 'A' to 'Z' is being encoded into numbers using the following encoding:</p>
<pre class="plaintext hljs"><code>'A' -&gt; 1
'B' -&gt; 2
.
.
.
'Y' -&gt; 25
'Z' -&gt; 26</code></pre>
<p>Given an encoded string, find the number of ways it can be decoded.</p>
<h5>Examples</h5>
<pre class="plaintext hljs"><code>decoded: 123
encoded: ["ABC", "LC", "AW"]
answer: 3</code></pre>
<pre class="plaintext hljs"><code>decoded: 36
encoded: ["CF"]
answer: 1</code></pre>
<pre class="plaintext hljs"><code>decoded: 106
encoded: ["JF"]
answer: 1</code></pre>
<pre class="plaintext hljs"><code>decoded: 306
encoded: []
answer: 0</code></pre>
<p>The total number of ways to decode can be larger than the largest 32 bit number. Return your answer with module 10<sup>9</sup> + 7.</p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.<br/>
For each test case, the input has a string denoting the decoded string</p>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with one integer denoting the total number of ways. Return the answer with module 10<sup>9</sup> + 7.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
123
36
106
306</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>3
1
1
0</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 30</code><br/>
<code>1 &lt;= length of string &lt;= 10<sup>4</sup></code><br/>
The string contains only digits and may contain leading zeroes</p>

---
# [Solution](solution.md)
