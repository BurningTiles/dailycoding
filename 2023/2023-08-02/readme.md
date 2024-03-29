
# 02 Aug 2023

# Questions

---
## [1. String Permutations](https://workat.tech/problem-solving/practice/string-permutations) [(LeetCode)](https://leetcode.com/problems/permutations/) 

<p>Given a string <code>s</code> with distinct lowercase English characters, find all the permutations of <code>s</code>.</p>
<h5>Example:</h5>
<pre class="plaintext hljs"><code>s: &ldquo;abc&rdquo;
Permutations:
&ldquo;abc&rdquo;
&ldquo;acb&rdquo;
&ldquo;bac&rdquo;
&ldquo;bca&rdquo;
&ldquo;cab&rdquo;
&ldquo;cba&rdquo;</code></pre>
<h3>Testing</h3>
<h4>Input Format&nbsp;</h4>
<p>The first line contains an integer &lsquo;T&rsquo;, denoting the number of test cases.</p>
<p>For each test case, the input has two lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the length of the string <code>s</code>.</li>
<li>The string &lsquo;s&rsquo;.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has <code>n!</code> lines. Each line has one of the permutations of <code>s</code>.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
4
abcd
1
a</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>abcd
abdc
acbd
acdb
adbc
adcb
bacd
badc
bcad
bcda
bdac
bdca
cabd
cadb
cbad
cbda
cdab
cdba
dabc
dacb
dbac
dbca
dcab
dcba
a</code></pre>
<h4>Constraint</h4>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n &lt;= 8</code></p>

---
# [Solution](solution.md)
