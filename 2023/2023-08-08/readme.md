
# 08 Aug 2023

# Questions

---
## [1. Consecutively Descending Integers](https://workat.tech/problem-solving/practice/consecutively-descending-integers) 

<p>Given a string containing digits, determine if the string can be broken into consecutively descending integers.</p>
<h5>Examples</h5>
<pre class="plaintext hljs"><code>String: "10099989796"
Answer: true
Explanation: [100, 99, 98, 97, 96]</code></pre>

<pre class="plaintext hljs"><code>String: "543210"
Answer: true
Explanation: [5, 4, 3, 2, 1, 0]</code></pre>

<pre class="plaintext hljs"><code>String: "54320"
Answer: false
Explanation: No way to create consecutive descending integers</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer ‘T’ denoting the number of test cases.</p>
<p>For each test case, the input has one line with the string ‘s’.</p>
<h4>Output Format</h4>
<p>For each test case, the output contains true/false.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
10099989796
543210
54320</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>true
true
false</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code></p>
<p><code>1 &lt;= length of s &lt;= 12</code></p>
<p>Each character of <code>s</code> is a digit.</p>

---
# [Solution](solution.md)
