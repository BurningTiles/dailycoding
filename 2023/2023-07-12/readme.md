
# 12 Jul 2023

# Questions

---
## [1. Remove Loop From Linked List](https://workat.tech/problem-solving/practice/remove-loop-linked-list) 

<p>Given a linked list, remove the loop if it exists.</p>
<p>You need to find the last node of the list that points to one of its previous nodes and make it point to <code>NULL</code>.</p>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/remove-loop-linked-list.png" alt="Remove Loop From Linked List" width=500 />
<h3>Testing</h3>
<h4>Input Format</h4>
<p>First line contains &lsquo;T&rsquo;, denoting the number of independent test cases.</p>
<p>For each test case, the input has three lines:</p>
<ul>
<li>A number &lsquo;n&rsquo;, denoting the length of the linked list.</li>
<li><em>n</em> space-separated integers denoting the elements of the linked list.&nbsp;</li>
<li>A number denoting the position of the node to which the last node is connected.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, it contains a line with <i>n</i> space space-separated integers denoting elements of the linked list.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>5
3
3 4 5
1
5
1 2 3 4 5
2
4
67 54 890 32
4
2
23 45
-1
0

-1</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>3 4 5
1 2 3 4 5
67 54 890 32
23 45

</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>0 &lt;= n &lt;= 1000</code><br/>
<code>1 &lt;= node elements &lt;= 10<sup>5</sup></code></p>

---
## [2. Flatten a Multi-Level Linked List](https://workat.tech/problem-solving/practice/flatten-multi-level-linked-list) 

<p>You are given a linked list structure, where each node has two pointers:</p>
<ul>
<li><strong>next</strong>: points to an identical node towards the right.</li>
<li><strong>down</strong>: points to an identical node towards the bottom.</li>
</ul>
<p>Only the top most node can have a non-NULL next pointer.</p>
<p>This gives us a set of vertical linked lists and a horizontal linked list with the head nodes of the vertical lists.</p>
<p>Also, all vertical lists are sorted.</p>
<p>Your task is to flatten the lists into a single linked list, which should also be sorted.</p>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/flatten-multi-level-linked-list.png" alt="Flatten a Multi-Level Linked List" />
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains &lsquo;T&rsquo; denoting no of test cases.</p>
<p>For each test case,</p>
<ul>
<li>The first line contains an integer &lsquo;n&rsquo; denoting the number of connected vertical linked lists.</li>
<li>The second line contains <em>n</em> space-separated integers L<sub>i</sub> denoting the length of each vertical linked list.</li>
<li>Next <em>n</em> lines contain L<sub>i</sub> space-separated integers denoting elements of the respective linked list.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, a line containing space-separated integers denoting the elements of flattened linked list.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>1
4
3 2 3 4
1 3 8
5 8
8 14 26
13 15 22 25</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 3 5 8 8 8 13 14 15 22 25 26</code></pre>
<p>Take a look at the diagram above to understand this better.</p>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 100</code><br/>
<code>1 &lt;= L<sub>i</sub> &lt;= 100</code><br/>
<code>1 &lt;= node value &lt;= 1000</code></p>

---
# [Solution](solution.md)
