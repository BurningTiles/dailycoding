
# 13 Sep 2023

# Questions

---
## [1. Power Set](https://workat.tech/problem-solving/practice/power-set) [(LeetCode)](https://leetcode.com/problems/subsets/) 

<p>You are given an integer array <code>nums</code>, composed of <strong>unique</strong> elements. Find its power set.<br/>
<i>Power set</i> is the collection of <i>all possible subsets</i> of a given set.<br/>
The result must <strong>not</strong> contain duplicates and can be in <strong>any order</strong>.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code><strong>nums:</strong> [1, 2, 3]
<strong>Power Set:</strong> [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.</p>
<p>For each test case, the input has two lines with the following:</p>
<ul>
<li>An integer <strong>n</strong>, denoting the size of the array <i>nums</i>.</li>
<li><i>n</i> space-separated integers denoting the elements of the array <i>nums</i>.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has <i>m</i> lines, where <i>m</i> is the number of subsets of <i>nums</i>.<br/>
Each line has space-separated integers denoting the subset.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
2
1 2
3
1 2 3</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>
1 
1 2 
2 

1 
1 2 
1 2 3 
1 3 
2 
2 3 
3 </code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10</code><br/>
<code>1 &lt;= nums<sub>i</sub> &lt;= 10</code></p>

---
# [Solution](solution.md)
