
# 01 Aug 2023

# Questions

---
## [1. Tug of War](https://workat.tech/problem-solving/practice/tug-of-war) [(LeetCode)](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/) 

<p>Given a set of n integers denoting the strength of each student participating in a tug of war, divide the students into 2 equal parts such that the difference between the strengths of both the groups is minimum. Return the difference between the strengths of both the groups.</p>
<p>Note: If the number of students is odd, one group will have an extra student.</p>
<h5>Examples</h5>
<pre class="plaintext hljs"><code>strengths: [1, 2, 3, 4]
group 1: [1, 4]
group 2: [2, 3]
difference: 0</code></pre>

<pre class="plaintext hljs"><code>strengths: [5, 1, 2, 8]
group 1: [1, 8]
group 2: [2, 5]
difference: 2</code></pre>

<pre class="plaintext hljs"><code>strengths: [1, 2, 3, 4, 5]
group 1: [1, 2, 5]
group 2: [3, 4]
difference: 1</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer ‘T’, denoting the number of test cases.</p>
<p>For each test case, the input has two lines.</p>
<ul>
<li>An integer ‘n’ denoting the length of the array strengths.</li>
<li>n space-separated unique integers denoting the elements of the array strengths.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains the min difference in strengths of the two groups.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
4
1 2 3 4
4
5 1 2 8
5
1 2 3 4 5</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>0
2
1</code></pre>
<h3>Constraint</h3>
<p><code>1 &lt;= T &lt;= 10</code></p>
<p><code>1 &lt;= n &lt;= 20</code></p>
<p><code>1 &lt;= A<sub>i</sub> &lt;= 500</code></p>

---
# [Solution](solution.md)
