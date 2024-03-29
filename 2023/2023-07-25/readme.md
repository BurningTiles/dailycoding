
# 25 Jul 2023

# Questions

---
## [1. Rat In A Maze](https://workat.tech/problem-solving/practice/rat-in-maze) 

<p>You are given a maze in the form of a matrix of size <code>n * m</code>. Each cell is either clear or blocked denoted by <code>1</code> and <code>0</code> respectively.<br />A rat sits at the top-left cell and there exists a block of cheese at the bottom-right cell. Both these cells are guaranteed to be clear.<br />You need to find if the rat can get the cheese if it can move only in one of the two directions - down and right. It can&rsquo;t move to blocked cells.</p>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/rat-in-maze.png" />
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo;, denoting the number of test cases.</p>
<p>For each test case the input has the following lines:</p>
<ul>
<li>The first line contains two space-separated integers &lsquo;n&rsquo; and &lsquo;m&rsquo; denoting the number of rows and columns of the matrix respectively.</li>
<li>The next <em>n</em> lines contain <em>m</em> space-separated integers which are either 0 or 1.</li>
</ul>
<h4>Output Format&nbsp;</h4>
<p>For each test case, a line containing <code>1</code> or <code>0</code> based on whether the rat can get the cheese or not respectively.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
4 4
1 1 0 0
1 1 1 1
0 1 0 1
0 1 0 1
4 4
1 1 0 0
1 1 1 1
0 1 1 0
0 1 0 1
4 5
1 0 1 1 1
1 1 1 0 1
0 1 0 0 1
0 1 1 0 1
3 4
1 0 0 0
0 0 0 0
0 0 1 1</code></pre>
<h4>Expected output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1
0
0
0</code></pre>
<h3>Constraint</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n, m &lt;= 100</code><br/>
<code>0 &lt;= maze<sub>ij</sub> &lt;= 1</code></p>

---
## [2. Subsets](https://workat.tech/problem-solving/practice/subsets) [(LeetCode)](https://leetcode.com/problems/subsets/) 

<p>Given an array of distinct integers A, return all possible subsets.</p>
<p>Note: The list should not contain any duplicate subsets.</p>
<h3>Example</h3>
<pre class="plaintext hljs"><code>A: [1, 3, 2]
Subsets: [
    [],
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 3],
    [2],
    [2, 3],
    [3]
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
1 3 2</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>2

5
4

2
2 4
4
8

1
1 2
1 2 3
1 3
2
2 3
3</code></pre>
<h3>Constraint</h3>
<p><code>1 &lt;= T &lt;= 10</code></p>
<p><code>1 &lt;= n &lt;= 10</code></p>
<p><code>1 &lt;= A<sub>i</sub> &lt;= 100</code></p>

---
# [Solution](solution.md)
