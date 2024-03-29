
# 06 Jul 2023

# Questions

---
## [1. Find xth Node from End of Linked List](https://workat.tech/problem-solving/practice/find-xth-node-end-linked-list) 

<p>Given a linked list, find the xth node from the end.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>Linked list: 1→2→3→4
x: 2
Result: 3</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer ‘T’ denoting the number of independent test cases.</p>
<p>For each test case the input has three lines:</p>
<ul>
<li>An integer ‘n’ denoting the length of the linked list.</li>
<li>n space-separated integers denoting elements of the linked list.</li>
<li>An integer ‘x’ denoting the xth element from the end to be found.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, an integer denoting the element to be found.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
3
3 4 5
2
3
1 2 3
1</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>4
3</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>1 &lt;= x &lt;= n &lt;= 10<sup>4</sup></code></p>
<p><code>1 &lt;= element &lt;= 1000</code></p>

---
## [2. Delete Xth Node From End of Linked List](https://workat.tech/problem-solving/practice/delete-xth-node-end-linked-list) [(LeetCode)](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) 

<p>Given a linked list, delete the x<sup>th</sup> node from the end.</p>
<h5>Example:</h5>
<p>Linked list: <code>1&rarr;2&rarr;3&rarr;4</code></p>
<p>x: <code>2</code></p>
<p>Result: <code>1&rarr;2&rarr;4</code></p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of independent test cases.</p>
<p>For each test case the input has three lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the length of the linked list.</li>
<li><em>n</em> space-separated integers denoting elements of the linked list.</li>
<li>An integer &lsquo;x&rsquo; denoting the x<sup>th</sup> element from the end to be deleted.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, a line which contains space-separated integers denoting the elements of the resultant link list.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
3
3 4 5
2
3
1 0 1
1</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>3 5
1 0</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n &lt;= 10<sup>4</sup></code><br/>
<code>1 &lt;= x &lt;= n</code><br/>
<code>1 &lt;= element &lt;= 10<sup>5</sup></code></p>

---
# [Solution](solution.md)
