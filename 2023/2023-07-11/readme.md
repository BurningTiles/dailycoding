
# 11 Jul 2023

# Questions

---
## [1. Rotate a Linked List](https://workat.tech/problem-solving/practice/rotate-linked-list) [(LeetCode)](https://leetcode.com/problems/rotate-list/) 

<p>Given a linked list, rotate it to the right by <strong>k</strong> nodes.</p>
<h5>Examples:</h5>
<p>Input: <code>1&rarr;2&rarr;3&rarr;4</code><br/>
k: <code>3</code><br/>
Output: <code>2&rarr;3&rarr;4&rarr;1</code></p>
<p>Input: <code>1&rarr;2&rarr;3</code><br/>
k: <code>4</code><br/>
Output: <code>3&rarr;1&rarr;2</code></p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo;, denoting the number of test cases.</p>
<p>For each test case the input has three lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the length of the linked list.</li>
<li><em>n</em> space-separated integers denoting elements of the linked list.</li>
<li>An integer &lsquo;k&rsquo; denoting the number of right-shifts you need to perform.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, a line containing space-separated elements of the linked list after rotation.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
4
5 4 3 1
2
5
1 2 3 4 5
6</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>3 1 5 4
5 1 2 3 4</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>0 &lt;= n &lt;= 10<sup>4</sup></code><br/>
<code>0 &lt;= k &lt;= 10<sup>9</sup></code><br/>
<code>1 &lt;= elements &lt;= 10<sup>5</sup></code></p>

---
## [2. Detect Loop in Linked List](https://workat.tech/problem-solving/practice/detect-loop-linked-list) [(LeetCode)](https://leetcode.com/problems/linked-list-cycle-ii/) 

<p>Given a linked list which can have a loop, find the node at which the loop starts. If no loop exists, return <code>NULL</code>.</p>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/detect-loop-linked-list.png" alt ="Detect Loop in Linked List" width=500 />
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of independent test cases.</p>
<p>For each test case the input has three lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the length of the linked list.</li>
<li><em>n</em> space-separated integers denoting elements of the linked list.</li>
<li>An integer &lsquo;m&rsquo; denoting the index of the node to which the last node is connected.</li>
</ul>
<p>Note: <i>m</i> is in the range [0, n-1] for valid loop. A value of -1 indicates no loop.</p>
<h4>Output Format</h4>
<p>For each test case, a line containing the value of the node at which the loop starts.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
3
3 4 5
1
4
1 2 3 4
0
3
5 6 7
-1</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>4
1
-1</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n &lt;= 10<sup>4</sup></code><br/>
<code>-1 &lt;= m &lt; n</code><br/>
<code>1 &lt;= node value &lt;= 10<sup>5</sup></code></p>

---
# [Solution](solution.md)
