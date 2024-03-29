
# 19 Sep 2023

# Questions

---
## [1. Longest Palindromic Substring (LPS)](https://workat.tech/problem-solving/practice/longest-palindromic-substring) [(LeetCode)](https://leetcode.com/problems/longest-palindromic-substring/) 

<p>Given a string, return the longest palindromic substring (LPS) in it.</p>
<p>Note: There can be multiple palindromic substrings with the max length. In case of conflict, return the substring that has the smallest starting index.</p>
<h5>Examples</h5>
<pre class="plaintext hljs"><code>str: "abcdcab"
LPS: "cdc"</code></pre>

<pre class="plaintext hljs"><code>str: "abcdcba"
LPS: "abcdcba"</code></pre>

<pre class="plaintext hljs"><code>str: "abcd"
LPS: "a"</code></pre>

<pre class="plaintext hljs"><code>str: "abaadcd"
LPS: "aba"</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.<br/>
For each test case, the input contains a string.</p>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with one string denoting the LPS.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>5
abcdcab
abcdcba
abcd
abaadcd
workattech</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>cdc
abcdcba
a
aba
tt</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= string length &lt;= 500</code><br/>
The string contains only lowercase english alphabets</p>

---
# [Solution](solution.md)
