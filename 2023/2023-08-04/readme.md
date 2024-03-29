
# 04 Aug 2023

# Questions

---
## [1. Generate Parentheses](https://workat.tech/problem-solving/practice/generate-parentheses) [(LeetCode)](https://leetcode.com/problems/generate-parentheses/) 

<p>Given a number <code>n</code> denoting n pairs of parentheses, return all valid expressions using the n pairs of parentheses.</p>
<h5>Examples</h5>
<pre class="plaintext hljs"><code>n: 2
Answer: [
    "(())",
    "()()",
]</code></pre>

<pre class="plaintext hljs"><code>n: 3
Answer: [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer ‘T’, denoting the number of test cases.</p>
<p>For each test case, the input has an integer n.</p>
<h4>Output Format</h4>
<p>For each test case, the output has multiple lines each denoting a valid parenthesis expression.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
1
2
3</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>()
(())
()()
((()))
(()())
(())()
()(())
()()()</code></pre>
<h3>Constraint</h3>
<p><code>1 &lt;= T &lt;= 8</code></p>
<p><code>1 &lt;= n &lt;= 8</code></p>

---
# [Solution](solution.md)
