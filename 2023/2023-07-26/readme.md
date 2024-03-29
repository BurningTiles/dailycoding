
# 26 Jul 2023

# Questions

---
## [1. Subsets - II](https://workat.tech/problem-solving/practice/subsets-ii) [(LeetCode)](https://leetcode.com/problems/subsets-ii/) 

<p>Given an array of integers A, return all possible subsets. The array might contain duplicates.</p>
<p>Note: The list should not contain any duplicate subsets.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>A: [1, 3, 3]
Subsets: [
    [],
    [1],
    [1, 3],
    [1, 3, 3],
    [3],
    [3, 3]
]</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer ‘T’, denoting the number of test cases.</p>
<p>For each test case, the input has two lines.</p>
<ul>
<li>An integer ‘n’ denoting the length of the array A.</li>
<li>n space-separated unique integers denoting the elements of the array A.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has the following lines:</p>
<ul>
<li>The first line contains an integer ‘m’ denoting the total no of subsets.</li>
<li>The next m line contains space-separated integers denoting elements in that particular subset.</li>
</ul>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
1
5
2
2 4
3
1 3 3</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>2

5
4

2
2 4
4
6

1
1 3
1 3 3
3
3 3</code></pre>
<h3>Constraint</h3>
<p><code>1 &lt;= T &lt;= 10</code></p>
<p><code>1 &lt;= n &lt;= 10</code></p>
<p><code>1 &lt;= A<sub>i</sub> &lt;= 100</code></p>

---
## [2. Subset Sum](https://workat.tech/problem-solving/practice/subset-sum) 

<p>Given an array of integers <code>A</code> and a target value <code>target</code>.</p>
<p>Find whether there exists a subset in the array <code>A</code> where their sum is equal to <code>target</code>.</p>
<h5>Example:</h5>
<p>A: <code>[1, 3, 4, 9, 2]</code></p>
<p>target: <code>13</code></p>
<p>Result: Subset exists.</p>
<p>Subset <code>[1, 3, 9]</code> has a sum equal to <code>13</code>.</p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo;, denoting the number of test cases.</p>
<p>For each test case the input has three lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the length of the array <code>A</code>.</li>
<li><em>n</em> space-separated integers denoting the elements of the array <code>A</code>.</li>
<li>An integer &lsquo;target&rsquo; denoting the target value.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has a line with <code>1</code> or <code>0</code> depending on whether the subset exists or not respectively.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
5
1 1 2 3 4
5
5
1 3 1 3 4
20</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1
0</code></pre>
<h4>Constraint</h4>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n &lt;= 16</code><br/>
<code>1 &lt;= A<sub>i</sub> &lt;= 500</code><br/>
<code>1 &lt;= target &lt;= 500</code></p>

---
# [Solution](solution.md)
