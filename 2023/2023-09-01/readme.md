
# 01 Sep 2023

# Questions

---
## [1. Binary Search Tree (BST) Iterator](https://workat.tech/problem-solving/practice/binary-search-tree-iterator) [(LeetCode)](https://leetcode.com/problems/binary-search-tree-iterator/) 

<p>Implement the <code>BSTIterator</code> class. The <code>BSTIterator</code> will be used to iterate over the inorder traversal of a BST.</p>
<ul>
<li><code>BSTIterator(root)</code> initializes an object of the BSTIterator class.</li>
<li><code>boolean hasNext()</code> returns whether there is a next element in the traversal.</li>
<li><code>Node next()</code> moves the pointer to the next node in the traversal and returns the node.</li>
</ul>
<p>Assume that <code>next()</code> will be called only if there is a next node.</p>
<p>The iterator would be called like this depending on your language:</p>
<pre class="java hljs"><code>BSTIterator iterator = new BSTIterator(root);
while iterator.hasNext() {
    print iterator.next()
}</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has 2 lines:</p>
<ul>
<li>The first line contains an integer <strong><em>n</em></strong> denoting the number of nodes in the tree (including the NULL nodes).</li>
<li>The second line contains <em>n</em> space-separated integers that will form the binary search tree. The integers follow level order traversal of the tree where -1 indicates a NULL node.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has a line containing the inorder traversal of the tree.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
9
2 1 3 -1 -1 -1 5 4 7
12
6 2 9 1 5 8 -1 -1 -1 4 -1 7
12
7 3 12 1 5 11 -1 -1 -1 4 -1 10
4
28 14 -1 11</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 2 3 4 5 7
1 2 4 5 6 7 8 9
1 3 4 5 7 10 11 12
11 14 28</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 10<sup>4</sup></code><br/>
<code>1 &lt;= node value &lt;= 10<sup>4</sup></code></p>

---
# [Solution](solution.md)
