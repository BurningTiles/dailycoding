
# 27 Jul 2023

# Questions

---
## [1. Combination Sum 1](https://workat.tech/problem-solving/practice/combination-sum-1) [(LeetCode)](https://leetcode.com/problems/combination-sum/) 

<p>Given an array of distinct integers <code>A</code> and a target value <code>val</code>, find all unique combinations of integers from <code>A</code> where their sum is equal to <code>val</code>.</p>
<p><strong>Note: </strong>Each integer may be used multiple times in the combination.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>A: [1, 2]
val: 4
Combinations: [
  [1, 1, 1, 1],
  [1, 1, 2],
  [2, 2]
]</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo;, denoting the number of test cases.</p>
<p>For each test case the input has three lines.</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the length of the array A.</li>
<li><em>n</em> space-separated unique integers denoting the elements of the array A.</li>
<li>An integer &lsquo;val&rsquo; denoting the target value.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has the following lines:</p>
<ul>
<li>The first line contains an integer &lsquo;m&rsquo; denoting the total no of distinct combinations.</li>
<li>The next <em>m</em> line contains space-separated integers denoting elements in that particular combination.</li>
</ul>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
2
1 2
4
5
1 3 4 5 6
4
5
1 2 3 4 8
7</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>3
1 1 1 1
1 1 2
2 2
3
1 1 1 1
1 3
4
11
1 1 1 1 1 1 1
1 1 1 1 1 2
1 1 1 1 3
1 1 1 2 2
1 1 1 4
1 1 2 3
1 2 2 2
1 2 4
1 3 3
2 2 3
3 4</code></pre>
<h3>Constraint</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 30</code><br/>
<code>1 &lt;= target &lt;= 500</code><br/>
<code>1 &lt;= A<sub>i</sub> &lt;= 500</code></p>

---
# [Solution](solution.md)
