
# 31 Jul 2023

# Questions

---
## [1. Combinations](https://workat.tech/problem-solving/practice/combinations) [(LeetCode)](https://leetcode.com/problems/combinations/) 

<p>Given two integers <code>n</code> and <code>k</code>, return all possible combinations of size k containing distinct numbers between 1 and n.</p>
<p>Note: The list should not contain any duplicate combinations.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>n: 4
k: 2
Combinations: [
    [1, 2],
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
    [3, 4]
]</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer ‘T’, denoting the number of test cases.</p>
<p>For each test case, the input has two integers n and k.</p>
<h4>Output Format</h4>
<p>For each test case, the output has the following lines:</p>
<ul>
<li>The first line contains an integer ‘m’ denoting the total no of combinations.</li>
<li>The next m line contains space-separated integers denoting elements in that particular combination.</li>
</ul>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
4 2
3 3
4 1</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>6
1 2
1 3
1 4
2 3
2 4
3 4
1
1 2 3
4
1
2
3
4</code></pre>
<h3>Constraint</h3>
<p><code>1 &lt;= T &lt;= 10</code></p>
<p><code>1 &lt;= k &lt;= n &lt;= 20</code></p>


---
# [Solution](solution.md)
