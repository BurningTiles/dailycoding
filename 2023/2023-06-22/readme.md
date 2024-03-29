
# 22 Jun 2023

# Questions

---
## [1. Flood Fill Image](https://workat.tech/problem-solving/practice/flood-fill-image) [(LeetCode)](https://leetcode.com/problems/flood-fill/) 

<p>Given an image as a matrix of colored cells. Each cell has a value ranging from <code>0</code> to <code>65535</code> denoting its color. You have to apply flood-fill to a particular cell of the matrix with color <code>c</code>.</p>
<p>Two cells are considered as part of the same connected component if they have a common side and the same color value.</p>
<p>When you apply flood-fill to a particular cell, all its connected components are also applied the same color.</p>
<img src="https://wat-images.s3.ap-south-1.amazonaws.com/images/ps/flood-fill-image.png" alt="Flood Fill Image" />
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo;, denoting the number of test cases.</p>
<p>For each test case the input has the following lines:</p>
<ul>
<li>The first line contains two space separated numbers, &lsquo;n&rsquo; and &lsquo;m&rsquo;, denoting the number of rows and columns of the matrix.</li>
<li>The next <em>n</em> lines contain <em>m</em> space-separated integers denoting the values at respective cells of the matrix.</li>
<li>The next line contains two integers &lsquo;x&rsquo; and &lsquo;y&rsquo; denoting the target row and column index of the cell to which flood fill is to be applied.</li>
<li>The next line contains an integer &lsquo;c&rsquo;, denoting the color to fill.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains <em>n</em> lines containing <em>m</em> space-separated integers denoting the resultant image.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>4
2 2
1 0
0 0
1 1
2
3 3
1 1 0
1 1 1
1 1 1
0 0
3
4 4
1 2 1 2
2 2 2 1
1 2 2 1
2 1 2 1
0 1
3
2 2
1 2
2 1
0 1
3</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>1 2
2 2
3 3 0
3 3 3
3 3 3
1 3 1 2
3 3 3 1
1 3 3 1
2 1 3 1
1 3
2 1</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 10</code><br/>
<code>1 &lt;= n, m &lt;= 500</code><br/>
<code>0 &lt;= color value &lt;= 65535</code><br/>
<code>0 &lt;= x &lt; n</code><br/>
<code>0 &lt;= y &lt; m</code><br/>
<code>0 &lt;= c &lt;= 65535</code></p>

---
## [2. Roman Numeral to Integer](https://workat.tech/problem-solving/practice/roman-to-integer) [(LeetCode)](https://leetcode.com/problems/roman-to-integer/) 

<p>Given a roman numeral <code>s</code>, convert it to an integer.</p>
<p>Roman numerals are denoted by a combination of some symbols.</p>
<table>
	<thead>
		<tr><th>Symbol</th><th>Value</th></tr>
	</thead>
	<tbody>
		<tr><td>I</td><td>1</td></tr>
		<tr><td>V</td><td>5</td></tr>
		<tr><td>X</td><td>10</td></tr>
		<tr><td>L</td><td>50</td></tr>
		<tr><td>C</td><td>100</td></tr>
		<tr><td>D</td><td>500</td></tr>
		<tr><td>M</td><td>1000</td></tr>
	</tbody>
</table>
<h5>Example 1</h5>
<p>s: <code>&ldquo;X&rdquo;</code></p>
<p>Result: <code>10</code></p>
<h5>Example 2</h5>
<p>s: <code>&ldquo;VI&rdquo;</code></p>
<p>Result: <code>6</code></p>
<h5>Example 3</h5>
<p>s: <code>&ldquo;XII&rdquo;</code></p>
<p>Result: <code>12</code></p>
<p><i>Read about Roman To Integer conversion <a target="_blank" rel="noopener noreferrer" href="https://www.math-only-math.com/roman-numerals.html">here</a></i>.</p>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.</p>
<p>For each test case, the input contains a line with string &lsquo;s&rsquo;.</p>
<h4>Output Format</h4>
<p>For each test case, the output contains one line with an integer &lsquo;val&rsquo; denoting the integer value.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
XV
MMMDCX
XX</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>15
3610
20</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= s.size &lt;= 15</code></p>

---
# [Solution](solution.md)
