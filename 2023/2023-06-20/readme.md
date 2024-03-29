
# 20 Jun 2023

# Questions

---
## [1. Adjacency List to Adjacency Matrix](https://workat.tech/problem-solving/practice/adjacency-list-to-adjacency-matrix) 

<p>Given the nodes and adjacency list of a graph, calculate the adjacency matrix for the it.</p>
<p>You have a graph with <code>n</code> nodes indexed from <code>0</code> to <code>n-1</code>. You are also given the adjacency list for each node.</p>
<p>You have to return the adjacency matrix for the given graph.</p>
<h5>Example</h5>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/adjacency-list-to-adjacency-matrix.svg" alt="adjacency-list-to-adjacency-matrix" width="100%"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has the following lines:</p>
<ul>
<li>The first line contains the integer <strong><em>n</em></strong>.</li>
<li>The next <i>n</i> lines descibes the adjacent nodes for the i<sup>th</sup> node.
	<ul>
		<li>The first integer <strong><em>m</em></strong> denotes the number of adjacent nodes.</li>
		<li>The next <i>m</i> integers denote adjacent nodes.</li>
	</ul>
</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has n lines denoting the adjacency matrix of the graph.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
4
3 1 2 3
1 0
2 0 3
2 0 2
4
3 1 2 3
1 0
2 0 3
3 0 2 3</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>0 1 1 1
1 0 0 0
1 0 0 1
1 0 1 0
0 1 1 1
1 0 0 0
1 0 0 1
1 0 1 1</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 500</code><br/>
<code>0 &lt;= m &lt;= n</code></p>

---
## [2. Adjacency Matrix to Adjacency List](https://workat.tech/problem-solving/practice/adjacency-matrix-to-adjacency-list) 

<p>Given the nodes and adjacency matrix of a graph, calculate the adjacency list for it.</p>
<p>You have a graph with <code>n</code> nodes indexed from <code>0</code> to <code>n-1</code>. You also have the adjacency matrix where each cell denotes whether two nodes are connected.</p>
<p>You have to return the adjacency list for the given graph.</p>
<h5>Example</h5>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/adjacency-matrix-to-adjacency-list.svg" alt="adjacency-matrix-to-adjacency-list" width="100%"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has the following lines:</p>
<ul>
<li>The first line contains the integer <strong><em>n</em></strong>.</li>
<li>The next <i>n</i> lines contain <i>n</i> space-separated integers each denoting the adjacency matrix.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has n lines denoting the adjacency list of the graph.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
4
0 1 1 1
1 0 0 0
1 0 0 1
1 0 1 0
4
0 1 1 1
1 0 0 0
1 0 0 1
1 0 1 1</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 2 3
0
0 3
0 2
1 2 3
0
0 3
0 2 3</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n &lt;= 500</code></p>

---
# [Solution](solution.md)
