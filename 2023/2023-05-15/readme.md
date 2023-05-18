
# 15 May 2023

# Questions

---
## [1. Unique Elements in Sorted Array](https://workat.tech/problem-solving/practice/unique-elements-sorted-array) [(LeetCode)](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) 

<p>Given a sorted array <code>A</code>, find the size of array <code>A</code> after removing the duplicate elements.</p>
<h5>Examples:</h5>
<p>A: <code>[1 2 3 3 3 4 5 5]</code></p>
<p>Size of <code>A</code> after removing duplicate elements: <code>5</code></p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.</p>
<p>For each test case, the input contains two lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the size of the array A.</li>
<li><em>n</em> space-separated integers denoting elements of the array A.</li>
</ul>
<h4>Output format</h4>
<p>For each test-cases, the output has a line with an integer &lsquo;len&rsquo; denoting the length of the resultant array.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
5
1 1 1 2 2
6
1 3 3 3 4 4</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>2
3</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n &lt;= 10<sup>4</sup></code><br/>
<code>1 &lt;= A<sub>i</sub> &lt;= 10<sup>5</sup></code></p>

---
## [2. Sorted Arrays Intersection](https://workat.tech/problem-solving/practice/sorted-arrays-intersection) 

<p>Given 2 sorted arrays, return the intersection of both the arrays. The intersection of 2 arrays means all the elements which are present in both.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>Array 1: [1, 3, 4, 5, 5, 6, 6, 7]
Array 2: [2, 5, 6, 6, 7, 8]
Intersection: [5, 6, 6, 7]</code></pre>

<p>Note: The resultant array should also be sorted.</p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer ‘T’ denoting the number of independent test cases.</p>
<p>For each test case, the input has three lines:</p>
<ul>
<li>The first line contains two integers ‘n’ and ‘m’ denoting the length of the arrays A and B respectively.</li>
<li>The second line contains n space-separated integers denoting the elements of A.</li>
<li>The third line contains m space-separated integers denoting the elements of B.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, print space-separated numbers denoting the intersection of the two sorted arrays.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
4 4
1 2 3 4
1 3 4 5
4 5
1 1 3 3
3 3 4 5 6
8 6
1 3 4 5 5 6 6 7
2 5 6 6 7 8</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 3 4
3 3
5 6 6 7</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>1 &lt;= n, m &lt;= 10<sup>4</sup></code></p>
<p><code>1 &lt;= A<sub>i</sub>, B<sub>i</sub> &lt;= 10<sup>5</sup></code></p>

---
# [Solution](solution.md)
