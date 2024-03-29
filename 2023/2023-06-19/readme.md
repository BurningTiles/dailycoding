
# 19 Jun 2023

# Questions

---
## [1. Best Time to Buy and Sell Stocks](https://workat.tech/problem-solving/practice/best-time-to-buy-and-sell-stock) [(LeetCode)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) 

<p>You are given an array <code>prices</code> where <code>prices[i]</code> denotes the price of a stock on the ith day. You want to maximize the profit by buying a stock and then selling it at a higher price.</p>
<p>Suppose you can make a single buy and single sell at any date after you buy, what is the maximum profit that you can make?</p>
<p>Note: Return 0 if you cannot make a profit.</p>
<h5>Examples</h5>
<pre class="plaintext hljs"><code>prices: [6, 1, 4, 2, 5, 3]
Answer: 4

<u>Explanation</u>
Buy on day 2 (price: 1) and Sell on day 5 (price: 5).
Profit: 5 - 1 = 4.</code></pre>
<pre class="plaintext hljs"><code>prices: [5, 4, 3, 2, 1]
Answer: 0

<u>Explanation</u>
No transactions that can give a profit.</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.<br/>
For each test case, the input has two lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the size of the array.</li>
<li><em>n</em> space-separated integers denoting the array.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with one integer denoting the max profit.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
6
6 1 4 2 5 3
5
5 4 3 2 1</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>4
0</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n &lt;= 10<sup>4</sup></code><br/>
<code>1 &lt;= prices<sub>i</sub> &lt;= 1000</code></p>

---
## [2. Best Time to Buy and Sell Stocks II](https://workat.tech/problem-solving/practice/best-time-to-buy-and-sell-stock-ii) [(LeetCode)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) 

<p>You are given an array <code>prices</code> where <code>prices[i]</code> denotes the price of a stock on the ith day. You want to maximize the profit by buying a stock and then selling it at a higher price.</p>
<p>Suppose you can do as many transactions as you want, what is the maximum profit that you can make?</p>
<p>Note:</p>
<ul>
<li>Return 0 if you cannot make a profit.</li>
<li>You cannot buy/hold more than 1 stock at a time.</li>
<li>You need to sell a stock before buying again.</li>
<li>You can sell a stock and buy it again on the same day.</li>
</ul>
<h5>Examples</h5>
<pre class="plaintext hljs"><code>prices: [6, 1, 4, 2, 5, 3]
Answer: 6

<u>Explanation</u>
Buy on day 2 (price: 1) and Sell on day 3 (price: 4).
Buy on day 4 (price: 2) and Sell on day 5 (price: 5).
Profit: (4 - 1) + (5 - 2) = 6.</code></pre>
<pre class="plaintext hljs"><code>prices: [1, 2, 3, 4, 5]
Answer: 4

<u>Explanation</u>
Buy on day 1 (price: 1) and Sell on day 5 (price: 5).
Profit: (5 - 1) = 4.</code></pre>
<h3>Testing</h3>
<h4>Input Format</h4>
<p>The first line contains an integer &lsquo;T&rsquo; denoting the number of test cases.<br/>
For each test case, the input has two lines:</p>
<ul>
<li>An integer &lsquo;n&rsquo; denoting the size of the array.</li>
<li><em>n</em> space-separated integers denoting the array.</li>
</ul>
<h4>Output Format</h4>
<p>For each test case, the output contains a line with one integer denoting the max profit.</p>
<h4>Sample Input</h4>
<pre class="plaintext hljs" id="sample-input"><code>2
6
6 1 4 2 5 3
5
1 2 3 4 5</code></pre>
<h4>Expected Output</h4>
<pre class="plaintext hljs" id="expected-output"><code>6
4</code></pre>
<h3>Constraints</h3>
<p><code>1 &lt;= T &lt;= 100</code><br/>
<code>1 &lt;= n &lt;= 10<sup>4</sup></code><br/>
<code>1 &lt;= prices<sub>i</sub> &lt;= 1000</code></p>

---
# [Solution](solution.md)
