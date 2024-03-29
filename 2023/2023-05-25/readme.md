
# 25 May 2023

# Questions

---
## [1. Intersection of Two Linked Lists](https://workat.tech/problem-solving/practice/intersection-two-linked-lists) [(LeetCode)](https://leetcode.com/problems/intersection-of-two-linked-lists/) 

<p>Given two linked lists, find the node at which they intersect.</p>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/intersection-linked-lists.svg" />
<p>Here the linked lists A and B intersect at C1.</p>
<p>If the two lists do not intersect, return <code>null</code>.</p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains &lsquo;T&rsquo; denoting the number of independent test cases.</p>
<p>For each test case, the input has five lines:</p>
<ul>
<li>Two space-separated integers L<sub>1</sub> and L<sub>2</sub> denoting the size of the lists A and B before they intersect.</li>
<li>L<sub>1</sub> space-separated integers denoting the node values for the first L<sub>1</sub> nodes of A.</li>
<li>L<sub>2</sub> space-separated integers denoting the node values for the first L<sub>2</sub> nodes of B.</li>
<li>An integer L<sub>3</sub> denoting the length of the list after A and B intersect.</li>
<li>L<sub>3</sub> space-separated integers denoting the node values for the common nodes of A and B.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, a line with the value of the node where A and B intersect. If they do not intersect, output -1.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
3 3
4 5 6
7 8 9
3
1 2 3
0 4

4 5 6 7
2
8 9
2 3
1 2
3 4 5
0

</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1
8
-1</code></pre>
<h4>Constraints</h4>
<p>1 &lt;= T &lt;= 10<br/>
0 &lt;= L<sub>1</sub>, L<sub>2</sub>, L<sub>3</sub> &lt;= 10<sup>4</sup><br/>
1 &lt;= nodeValue &lt; = 10<sup>5</sup></p>

---
## [2. Remove Duplicates from Sorted Linked List](https://workat.tech/problem-solving/practice/remove-duplicates-sorted-linked-list) [(LeetCode)](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) 

<p>Given a sorted linked list, remove all duplicates from the Linked List.</p>
<p>After the operation, every element should appear only once. Do not change the order of the linked list.</p>
<h5>Example</h5>
<pre class="plaintext hljs"><code>Linked List: 1→2→2→2→3→3→4→7
After removing duplicates: 1→2→3→4→7</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains ‘T’ denoting the number of independent test cases.</p>
<p>For each test case the input has two lines:</p>
<ul>
<li>A number ‘n’, denoting the length of the linked list.</li>
<li>n space-separated integers denoting elements of the linked list.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has one line with space-separated integers denoting the elements of the resultant linked list.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
8
1 2 2 2 3 3 4 7
3
4 5 6</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 2 3 4 7
4 5 6</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code></p>
<p><code>0 &lt;= n &lt;= 10<sup>4</sup></code></p>
<p><code>1 &lt;= element &lt;= 10<sup>4</sup></code></p>

---
# [Solution](solution.md)
