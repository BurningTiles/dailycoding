
# 07 Jul 2023

# Questions

---
## [1. Add Two Numbers as Lists](https://workat.tech/problem-solving/practice/add-numbers-lists) [(LeetCode)](https://leetcode.com/problems/add-two-numbers/) 

<p>Given two natural numbers, <code>a</code> and <code>b</code>, represented as reversed linked lists, compute their sum c as another reversed linked list.</p>
<h4>Example 1</h4>
<p>Two numbers 132 and 541 are shown in the form of reversed linked lists, and so is their sum which is 673.</p>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/add-numbers-lists.png" alt="Add Two Numbers as Lists" width=500 />
<h5>Example 2</h5>
<p><i>Input:</i><br/>
a: 321 : &nbsp; 1 &rarr; 2 &rarr; 3<br/>
b: 654 : &nbsp; 4 &rarr; 5 &rarr; 6</p>
<p><i>Output:</i><br/>
c: 975 : &nbsp; 5 &rarr; 7 &rarr; 9</p>
<h5>Example 3</h5>
<p><i>Input:</i><br/>
a: 501 : &nbsp; 1 &rarr; 0 &rarr; 5<br/>
b: 639 : &nbsp; 9 &rarr; 3 &rarr; 6</p>
<p><i>Output:</i><br/>
c: 1140 : &nbsp; 0 &rarr; 4 &rarr; 1 &rarr; 1</p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>For each test case, the input has three lines:</p>
<ul>
<li>Two space-separated integers, &lsquo;n&rsquo; and &lsquo;m&rsquo;, denoting the length of two numbers.</li>
<li><i>n</i> space-separarted numbers denoting digits of &lsquo;a&rsquo; in reverse order.</li>
<li><i>m</i> space-separarted numbers denoting digits of &lsquo;b&rsquo; in reverse order.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has a line with space separated digits of &lsquo;c&rsquo; in reverse order.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
3 3
3 4 5
1 0 1
1 4
3
1 2 3 4
3 3
3 4 5
3 0 1
1 2
3
3 4</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>4 4 6
4 2 3 4
6 4 6
6 4</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br />
<code>1 &lt;= n, m &lt;= 1000</code></p>

---
## [2. Reverse a Linked List II](https://workat.tech/problem-solving/practice/reverse-linked-list-ii) [(LeetCode)](https://leetcode.com/problems/reverse-linked-list-ii/) 

<p>Given a linked list and two numbers left and right, reverse the nodes from position '<code>left</code>' to position '<code>right</code>'. Assume: <code>left &lt;= right</code>.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>left: 2, right: 4
Linked list: 1→<span style="background-color: yellow;">5→7→13</span>
Result: 1→<span style="background-color: yellow;">13→7→5</span></code></pre>

<pre class="plaintext hljs"><code>left: 2, right: 3
Linked list: 1→<span style="background-color: yellow;">5→7</span>→13
Result: 1→<span style="background-color: yellow;">7→5</span>→13</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer ‘T’ denoting the number of independent test cases.</p>
<p>For each test case the input has three lines:</p>
<ul>
<li>An integer ‘n’ denoting the length of the linked list.</li>
<li>n space-separated integers denoting elements of the linked list.</li>
<li>Two integers: left and right.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, a line containing ‘n’ space-separated integers denoting the resultant linked list elements.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
4
1 5 7 13
2 4
4
1 5 7 13
2 3
4
1 5 7 13
3 3</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 13 7 5
1 7 5 13
1 5 7 13</code></pre>

<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>1 &lt;= left &lt;= right &lt;= n &lt;= 10<sup>4</sup></code></p>
<p><code>1 &lt;= key &lt;= 1000</code></p>

---
# [Solution](solution.md)
