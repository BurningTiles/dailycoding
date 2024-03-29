
# 13 Jul 2023

# Questions

---
## [1. Partition List](https://workat.tech/problem-solving/practice/partition-list) [(LeetCode)](https://leetcode.com/problems/partition-list/) 

<p>Given a linked list and a key, partition it such that all nodes with values less than key are before it and all nodes with values greater than key are after it.</p>
<p>The relative order of the numbers in each of the partition should be maintained.</p>
<pre class="plaintext hljs"><code>Linked list: 1 → 6 → 2 → 4 → 3 → 5 → 2 → 8 → 4 → 7
key: 5
Result: <span style="background-color: yellow">1 → 2 → 4 → 3 → 2 → 4</span> → 5 → <span style="background-color: yellow">6 → 8 → 7</span></code></pre>

<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer ‘T’ denoting the number of independent test cases.</p>
<p>For each test case the input has three lines:</p>
<ul>
<li>An integer ‘n’ denoting the length of the linked list.</li>
<li>n space-separated integers denoting elements of the linked list.</li>
<li>An integer 'key' denoting the pivot element.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, a line containing ‘n’ space-separated integers denoting the resultant linked list elements.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
10
1 6 2 4 3 5 2 8 4 7
5
10
1 6 2 4 3 5 2 8 4 7
8</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 2 4 3 2 4 5 6 8 7
1 6 2 4 3 5 2 4 7 8</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 1000</code></p>
<p><code>1 &lt;= n &lt;= 1000</code></p>
<p><code>1 &lt;= key &lt;= 1000</code></p>
<p><code>1 &lt;= element &lt;= 1000</code></p>


---
## [2. Insertion Sort Linked List](https://workat.tech/problem-solving/practice/insertion-sort-linked-list) [(LeetCode)](https://leetcode.com/problems/insertion-sort-list/) 

<p>Given a linked list, sort it using insertion sort.</p>
<pre class="plaintext hljs"><code>Linked list: 1 → 6 → 2 → 4 → 3 → 5 → 2 → 8 → 4 → 7
Result: 1 → 2 → 2 → 3 → 4 → 4 → 5 → 6 → 7 → 8</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer ‘T’ denoting the number of independent test cases.</p>
<p>For each test case the input has two lines:</p>
<ul>
<li>An integer ‘n’ denoting the length of the linked list.</li>
<li>n space-separated integers denoting elements of the linked list.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, a line containing ‘n’ space-separated integers denoting the resultant linked list elements.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
10
1 6 2 4 3 5 2 8 4 7
10
1 2 2 3 4 4 5 6 7 8</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 2 2 3 4 4 5 6 7 8
1 2 2 3 4 4 5 6 7 8</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>1 &lt;= n &lt;= 500</code></p>
<p><code>1 &lt;= element &lt;= 500</code></p>


---
# [Solution](solution.md)
