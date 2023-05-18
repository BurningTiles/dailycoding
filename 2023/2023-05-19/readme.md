
# 19 May 2023

# Questions

---
## [1. Remove Element at Kth Position in Linked List](https://workat.tech/problem-solving/practice/delete-kth-element-linked-list) 

<p>Given a Linked List and an integer k, remove the element at the kth position of the linked list.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>List: 1→3→4→7
k: 2
Result: 1→4→7</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains ‘T’ denoting the number of independent test cases.</p>
<p>For each test case the input has three lines:</p>
<ul>
<li>A number ‘n’, denoting the length of the linked list.</li>
<li>n space-separated integers denoting elements of the linked list.</li>
<li>k denoting the position</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has one line with space-separated integers.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
4
1 3 4 7
2
3
4 5 6
1</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 4 7
5 6</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>1 &lt;= n &lt;= 1000</code></p>
<p><code>1 &lt;= k &lt;= n</code></p>
<p><code>1 &lt;= element &lt;= 1000</code></p>

---
## [2. Append Linked Lists](https://workat.tech/problem-solving/practice/append-linked-lists) 

<p>Given two Linked Lists, append second Linked List to end of first Linked List and return the first list.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>List 1: 1→3→4→7
List 2: 6→2→5
Result: 1→3→4→7→6→2→5</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains ‘T’ denoting the number of independent test cases.</p>
<p>For each test case the input has three lines:</p>
<ul>
<li>'n' and 'm', denoting the length of the linked lists.</li>
<li>n space-separated integers denoting elements of the first linked list.</li>
<li>m space-separated integers denoting elements of the second linked list.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has one line with space-separated integers.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
4 3
1 3 4 7
6 2 5
1 3
3
4 5 6</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 3 4 7 6 2 5
3 4 5 6</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>1 &lt;= n, m &lt;= 1000</code></p>
<p><code>1 &lt;= element &lt;= 1000</code></p>

---
# [Solution](solution.md)
