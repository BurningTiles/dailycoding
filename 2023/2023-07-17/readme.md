
# 17 Jul 2023

# Questions

---
## [1. Next Greater Element](https://workat.tech/problem-solving/practice/next-greater-element) 

<p>Given an array of positive integers <strong><code>A</code></strong>, find the first greater number for every element on its right. If a greater number does not exist, use <code>-1</code>.</p>
<h5>Example:</h5>
<p>Input: <code>[1, 5, 2, 3, 5]</code><br/>
Output: <code>[5, -1, 3, 5, -1]</code></p>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo;, denoting the number of test cases.</p>
<p>For each test case the input has two lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the length of the array.</li>
<li><em>n</em> space-separated integers denoting elements of the array.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, a line containing space-separated elements of the result.&nbsp;</p>
<h4>Sample Input&nbsp;</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
5
1 5 2 3 5
4
1 2 3 4
5
3 2 1 4 5
4
4 3 2 1</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>5 -1 3 5 -1
2 3 4 -1
4 4 4 5 -1
-1 -1 -1 -1</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n &lt;= 10<sup>4</sup></code><br/>
<code>1 &lt;= A<sub>i</sub> &lt;= 10<sup>5</sup></code></p>

---
## [2. Simplify Directory Path](https://workat.tech/problem-solving/practice/simplify-directory-path) [(LeetCode)](https://leetcode.com/problems/simplify-path/) 

<p>Given a string '<code>path</code>' representing the absolute path of a file in a Unix-like file system, simplify it.</p>
<p>Note:</p>
<ul>
<li>Absolute path will always start with a '/'.</li>
<li>A period '.' refers to the current directory.</li>
<li>A double period '..' refers to the parent directory.</li>
<li>Simplified path:</li>
<ul>
<li>Starts with a '/'</li>
<li>Any two directories are separated by a '/'.</li>
<li>Does not end with a '/' unless it is the root path.</li>
<li>Should only contain directories from root path to target file/directory and does not contain '.' or '..'.</li>
</ul>
</ul>
<h5>Examples</h5>
<pre class="plaintext hljs"><code>Absolute Path: "/home/"
Simplified Path: "/home"</code></pre>

<pre class="plaintext hljs"><code>Absolute Path: "/../"
Simplified Path: "/"</code></pre>

<pre class="plaintext hljs"><code>Absolute Path: "/a/./b/../../c/../d/"
Simplified Path: "/d"</code></pre>

<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo;, denoting the number of test cases.</p>
<p>For each test case the input contains a single line with a string denoting the absolute path.</p>
<h4>Output Format</h4>
<p>For each test case, a line containing a string denoting the simplified path.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
/home/
/../
/a/./b/../../c/../d/</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>/home
/
/d</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>1 &lt;= n &lt;= 3000</code></p>
<p><code>Valid characters in path: a-z, 0-9, '.', '/'</code></p>

---
# [Solution](solution.md)
