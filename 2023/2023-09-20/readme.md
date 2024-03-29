
# 20 Sep 2023

# Questions

---
## [1. Edit Distance (Levenshtein Distance)](https://workat.tech/problem-solving/practice/edit-distance) [(LeetCode)](https://leetcode.com/problems/edit-distance/description/) 

<p>You are given two strings <code>s1</code> and <code>s2</code>. Find the minimum number of operations required to convert <code>s1</code> to <code>s2</code>.</p>
<p>Permitted Operations:</p>
<ul>
<li>Insert a character</li>
<li>Delete a character</li>
<li>Replace a character</li>
</ul>
<p>Strings <code>s1</code> and <code>s2</code> are composed of only lowercase English characters.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>s1: "hello"
s2: "seldom"
Result: 3
Explanation:
hello &rarr; sello (replace h with s)
sello &rarr; seldo (replace l with d)
seldo &rarr; seldom (insert m at end)</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.<br/>
For each test case, the input has two lines:</p>
<ul>
<li>A string s1.</li>
<li>A string s2.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with one integer denoting the minimum number of operations required.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>5
hello
seldom
workattech
workattech
abc
def
ab
ba
workat
word</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>3
0
3
2
3</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= s1.length, s2.length &lt;= 400</code><br/></p>

---
# [Solution](solution.md)
