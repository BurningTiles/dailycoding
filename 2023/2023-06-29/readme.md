
# 29 Jun 2023

# Questions

---
## [1. Inversion Count](https://workat.tech/problem-solving/practice/inversion-count) 

<p>The inversion count of an array denotes how far is the array from being sorted.</p>
<p>If the array is sorted, inversion count is 0. If the array is sorted in reverse order, the inversion count is maximum.</p>
<p>More formally, the inversion count of an array <code>A</code> is the number of pairs (i, j) such <code>A[i] &lt; A[j]</code> and <code>i &gt; j</code>.</p>
<h5>Example</h5>
<p>Lets take the following array:<br /><code>8, 4, 1, 2</code></p>
<p>This array has an inversion count of 5.<br />(8, 4), (8, 1), (8, 2), (4, 1), (4, 2)</p>
<p>Given an array A, calculate the inversion count of the array.</p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>First-line contains &lsquo;T&rsquo; denoting the number of test cases.</p>
<p>For each test case</p>
<ul>
<li>The first line contains an integer &lsquo;n&rsquo; denoting the length of the array.</li>
<li>The second line contains n space-separated integers of the array.</li>
</ul>
<h4>Output Format</h4>
<p>One line for each test-case, denoting the inversion count of the array.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
5
1 1 2 2 3
3
3 2 1
5
10 1 2 3 4</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>0
3
4</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>4</sup></code><br/>
<code>1 &lt;= A<sub>i</sub> &lt;= 10<sup>5</sup></code></p>

---
## [2. Search Rotated Sorted Array](https://workat.tech/problem-solving/practice/search-rotated-array) [(LeetCode)](https://leetcode.com/problems/search-in-rotated-sorted-array/) 

<p>You are given a list of unique integers which are sorted but rotated at some pivot. You are also given a target value and you have to find its index in the list. If it is not present in the list, return -1.</p>
<p><strong>Example:</strong><br />
List: <code>[4, 5, 6, 7, 1, 2, 3]</code><br />
Target value: <code>6</code><br />
Resultant index: <code>2</code></p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains 'T', denoting the number of test cases.</p>
<p>Each test contains 3 lines:</p>
<ul>
<li>a number 'n', denoting the number of elements.</li>
<li><i>n</i> space-separated numbers denoting the array elements.</li>
<li>the target value.</li>
</ul>
<h4>Output Format</h4>
<p>T lines, each containing a number denoting the index of the target value. -1 if the target value is not present.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
7
4 5 6 7 0 1 2
4
4
3 4 1 2
5
5
5 1 2 3 4
2
4
5 6 3 4
4</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>0
-1
2
3</code></pre>
<h4>Constraints</h4>
<p><code>1 &lt;= T &lt;= 100</code><br />
<code>1 &lt;= n &lt;= 10<sup>4</sup></code><br />
<code>1 &lt;= array elements &lt;= 10<sup>6</sup></code><br />
<code>1 &lt;= target &lt;= 10<sup>6</sup></code></p>

---
# [Solution](solution.md)