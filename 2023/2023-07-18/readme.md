
# 18 Jul 2023

# Questions

---
## [1. Rotting Apples](https://workat.tech/problem-solving/practice/rotting-apples) [(LeetCode)](https://leetcode.com/problems/rotting-oranges/) 

<p>You are given an <code>n * m</code> grid where each position can contain one of the three values:</p>
<table>
	<thead>
		<tr><th>Cell Value</th><th>Represents</th></tr>
	</thead>
	<tbody>
		<tr><td>0</td><td>Empty Cell</td></tr>
		<tr><td>1</td><td>Fresh Apple</td></tr>
		<tr><td>2</td><td>Rotten Apple</td></tr>
	</tbody>
</table>
<p>Every day, all fresh apples which are adjacent to any rotten apple become rotten.</p>
<p>Two cells are adjacent if they have a common edge, i.e., each cell can have upto four adjacent cells.</p>
<p>Find the minimum number of days required for all the apples to be rotten. If this is not possible return <code>-1</code>.</p>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/rotting-apples.png" alt="Rotting Apples" />
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of independent test cases.</p>
<p>For each test case the input has the following lines:</p>
<ul>
<li>The first line contains two space separated numbers, &lsquo;n&rsquo; and &lsquo;m&rsquo;, denoting the number of rows and columns in the grid respectively.</li>
<li>The next n lines contain m elements each, denoting the elements of the grid.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, a line containing the minimum number of days for all the apples to be rotten.<br />If it is impossible, the value is <code>-1</code>.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
3 3
2 1 0
1 1 0
0 1 1
3 3
2 1 1
1 1 0
1 0 1</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>4
-1</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n, m &lt;= 200</code><br/>
<code>0 &lt;= cell value &lt;= 2</code></p>

---
## [2. Non-Repeating Element](https://workat.tech/problem-solving/practice/non-repeating-element) [(LeetCode)](https://leetcode.com/problems/single-element-in-a-sorted-array/) 

<p>Given a sorted list of numbers in which all elements appear twice except one element that appears only once, find the number that appears only once.</p>
<h4>Example:</h4>
<pre class="plaintext hljs"><code>1, 1, 2, 3, 3, 4, 4</code></pre>
<p>Here, &lsquo;2&rsquo; appears once and all other elements appear twice.</p>
<pre class="plaintext hljs"><code>findNonRepeatingElement([1, 1, 2, 3, 3, 4, 4]) =&gt; 2</code></pre>
<p><strong>Expected Time Complexity: O(log n)</strong></p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains 'T', denoting the no. of test cases.</p>
<p>Each test case consists of two lines. The first contains a number 'n' denoting the number of elements. The second line has &lsquo;n&rsquo; space-separated numbers denoting the elements.</p>
<h4>Output Format</h4>
<p>For each test case, a line containing the non-repeating number.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
1
3
3
1 2 2
5
3 3 4 4 5</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>3
1
5</code></pre>
<h4>Constraints</h4>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= Size of array &lt;= 20000</code><br/>
<code>1 &lt;= Elements in array &lt;= 10<sup>6</sup></code></p>

---
# [Solution](solution.md)
