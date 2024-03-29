
# 28 Jun 2023

# Questions

---
## [1. Merge Overlapping Intervals](https://workat.tech/problem-solving/practice/merge-overlap-intervals) [(LeetCode)](https://leetcode.com/problems/merge-intervals/) 

<p>Given a list of intervals, merge them to get a list of non-overlapping intervals.</p>
<p><code>interval<sub>i</sub> = [start<sub>i</sub>, end<sub>i</sub>]</code></p>
<p>Example:<br />
Intervals: <code>[[1, 2], [2, 3], [1, 4], [5, 6]]</code></p>
<p><code>[1, 2]</code> and <code>[2, 3]</code> can be merged to form <code>[1, 3]</code>.<br/>
Now, <code>[1, 3]</code> and <code>[1, 4]</code> can be merged to form <code>[1, 4]</code>.<br/>
<code>[1, 4]</code> and <code>[5, 6]</code> have no intersection.<br/>
Hence above intervals are merged to form:<br/>
<code>[[1, 4], [5, 6]]</code></p>
<p>Note that the final list should be in ascending order.</p>
<h3>Testing</h3>
<h4>Input format</h4>
<p>First-line contains &lsquo;T&rsquo;, denoting the number of independent test-cases.</p>
<p>For each test-case,</p>
<ul>
<li>The first line contains one integer &lsquo;n&rsquo; denoting the number of intervals.</li>
<li>The next <i>n</i> line contains 2 integers &lsquo;start&rsquo; and &lsquo;end&rsquo; denoting the start and end value of the interval.</li>
</ul>
<h4>Output format</h4>
<p>For each test-case,</p>
<ul>
<li>The first line contains &lsquo;m&rsquo;, denoting the no of intervals after merging.</li>
<li>The next <i>m</i> line contains 2 integers &lsquo;start&rsquo; and &lsquo;end&rsquo; denoting the start and end value of the interval.</li>
</ul>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>3
3
1 1
2 2
3 3
3
1 4
6 7
4 5
3
1 2
2 3
5 5</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>3
1 1
2 2
3 3
2
1 5
6 7
2
1 3
5 5</code></pre>
<h4>Constraints</h4>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n &lt;= 10<sup>4</sup></code><br/>
<code>1 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>9</sup></code></p>

---
## [2. Kth Largest Element](https://workat.tech/problem-solving/practice/kth-largest-element) [(LeetCode)](https://leetcode.com/problems/kth-largest-element-in-an-array/) 

<p>Given a list of numbers below:<br />
<code>4, 3, 6, 4, 1</code></p>
<p>What is the largest element in the list? &rarr; 6</p>
<p>What is the 3rd largest element in the list? &rarr; 4</p>
<p>Given a list of numbers, find the k<sup>th</sup> largest element in the list.</p>
<blockquote><p>A simple solution is to sort the array and get the kth largest element. The best sorting algorithms have an average case time complexity of O(n log n).</p><p>Try to solve this problem with an average time complexity of O(n).<br />Hint: <a target="_blank" rel="noopener noreferrer" href="https://en.wikipedia.org/wiki/Quickselect">Quickselect</a></p></blockquote>
<h3>Testing</h3>
<h4>Input format</h4>
<p>The first line contains &lsquo;T&rsquo; denoting the number of independent test cases.</p>
<p>For each test case,</p>
<ul>
<li>The first line contains &lsquo;n&rsquo;, denoting the length of the list.</li>
<li>The second line contains <i>n</i> space-separated integers denoting the elements of the list.</li>
<li>The third line contains &lsquo;k&rsquo; denoting the k<sup>th</sup> largest element to be found.</li>
</ul>
<h4>Output format</h4>
<p>For each test case, one line containing an integer denoting the kth largest element.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
4
4 3 2 1
2
5
1 2 3 4 5
1</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>3
5</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br>
<code>1 &lt;= n &lt;= 10<sup>4</sup></code><br/>
<code>1 &lt;= element &lt;= 10<sup>5</sup></code><br/>
<code>1 &lt;= k &lt;= n</code></p>

---
# [Solution](solution.md)