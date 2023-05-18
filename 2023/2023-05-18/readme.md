
# 18 May 2023

# Questions

---
## [1. Kth Element in Linked List](https://workat.tech/problem-solving/practice/kth-element-linked-list) 

<p>Given a Linked List, find the element at the kth position.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>List: 1→3→4→7
k: 2
Answer: 3</code></pre>
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
<pre class="plaintext hljs" id="expected-output"><code>3
4</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>1 &lt;= n &lt;= 1000</code></p>
<p><code>1 &lt;= k &lt;= n</code></p>
<p><code>1 &lt;= element &lt;= 1000</code></p>

---
## [2. Add Element at Kth Position in Linked List](https://workat.tech/problem-solving/practice/add-kth-element-linked-list) 

<p>Given a Linked List, an integer k and an element, add that element at the kth position of the linked list.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>List: 1→3→4→7
k: 2
Element: 5
Result: 1→5→3→4→7</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains ‘T’ denoting the number of independent test cases.</p>
<p>For each test case the input has three lines:</p>
<ul>
<li>A number ‘n’, denoting the length of the linked list.</li>
<li>n space-separated integers denoting elements of the linked list.</li>
<li>k and val denoting the position and the new element value</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has one line with space-separated integers.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
4
1 3 4 7
2 5
3
4 5 6
1 1</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 5 3 4 7
1 4 5 6</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>1 &lt;= n &lt;= 1000</code></p>
<p><code>1 &lt;= k &lt;= n</code></p>
<p><code>1 &lt;= element &lt;= 1000</code></p>

---
# [Solution](solution.md)
