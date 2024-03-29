
# 15 Sep 2023

# Questions

---
## [1. Longest Common Subsequence (LCS)](https://workat.tech/problem-solving/practice/longest-common-subsequence) 

<p>Given two strings <code>s1</code> and <code>s2</code>, find the length of their <i>longest common subsequence (LCS)</i>. If there is no common subsequence, return <code>0</code>.</p>
<p>The strings are composed of lower case English alphabets.</p>
<p>A subsequence of a string is a string that can be derived by deleting some or no characters such that the order of the remaining characters remain the same.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>s1: "workattech"
s2: "branch"
Result: 4
Explanation: Longest common subsequence is "rach"</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.<br/>
For each test case, the input has two lines:</p>
<ul>
<li>The string s1.</li>
<li>The string s2.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with one integer denoting the length of the longest common subsequence.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
workattech
branch
helloworld
playword
hello
hello
abc
def</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>4
5
5
0</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= s1.length, s2.length &lt;= 3000</code></p>

---
# [Solution](solution.md)
