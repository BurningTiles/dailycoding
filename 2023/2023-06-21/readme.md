
# 21 Jun 2023

# Questions

---
## [1. Edges to Adjacency Matrix](https://workat.tech/problem-solving/practice/edges-to-adjacency-matrix) 

<p>Given the nodes and edges of a graph, calculate the adjacency matrix for the graph.</p>
<p>You have a graph with <code>n</code> nodes indexed from <code>0</code> to <code>n-1</code>. You also have <code>m</code> bi-directional edges each connecting a couple of nodes.</p>
You have to return the adjacency matrix for the given graph.
<h5>Example</h5>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/edges-to-adjacency-matrix.svg" alt="edges-to-adjacency-matrix" width="100%"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has the following lines:</p>
<ul>
<li>The first line contains two space-separated integers <strong><em>n</em></strong> and <strong><em>m</em></strong>.</li>
<li>The next m lines contain two space-separated integers each denoting the edges.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has n lines denoting the adjacency matrix of the graph.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
4 4
0 1
0 2
2 3
0 3
4 5
0 1
2 0
2 3
3 3
0 3</code></pre>
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
<code>0 &lt;= m &lt;= n<sup>2</sup></code></p>

---
## [2. Edges to Adjacency List](https://workat.tech/problem-solving/practice/edges-to-adjacency-list) 

<p>Given the nodes and edges of a graph, calculate the adjacency list for the graph.</p>
<p>You have a graph with <code>n</code> nodes indexed from <code>0</code> to <code>n-1</code>. You also have <code>m</code> bi-directional edges each connecting a couple of nodes.</p>
You have to return the adjacency list for the given graph.
<h5>Example</h5>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/edges-to-adjacency-list.svg" alt="edges-to-adjacency-list" width="100%"/>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer <strong><em>T</em></strong> denoting the number of test cases.</p>
<p>For each test case, the input has the following lines:</p>
<ul>
<li>The first line contains two space-separated integers <strong><em>n</em></strong> and <strong><em>m</em></strong>.</li>
<li>The next m lines contain two space-separated integers each denoting the edges.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output has n lines denoting the adjacency list of the graph.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
4 4
0 1
0 2
2 3
0 3
4 5
0 1
2 0
2 3
3 3
0 3</code></pre>
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
<code>1 &lt;= n &lt;= 500</code><br/>
<code>0 &lt;= m &lt;= n<sup>2</sup></code></p>

---
# [Solution](solution.md)
