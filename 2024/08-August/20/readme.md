# 20 Aug 2024

# Questions

---
## [1140. Stone Game II](https://leetcode.com/problems/stone-game-ii)

<div class="elfjS" data-track-load="description_content"><p>Alice and Bob continue their games with piles of stones.  There are a number of piles <strong>arranged in a row</strong>, and each pile has a positive integer number of stones <code>piles[i]</code>.  The objective of the game is to end with the most stones. </p>
<p>Alice and Bob take turns, with Alice starting first.  Initially, <code>M = 1</code>.</p>
<p>On each player's turn, that player can take <strong>all the stones</strong> in the <strong>first</strong> <code>X</code> remaining piles, where <code>1 &lt;= X &lt;= 2M</code>.  Then, we set <code>M = max(M, X)</code>.</p>
<p>The game continues until all the stones have been taken.</p>
<p>Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.</p>
<p> </p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> piles = [2,7,9,4,4]
	<strong>Output:</strong> 10
	<strong>Explanation:</strong>  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
	</pre>
<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> piles = [1,2,3,4,5,100]
	<strong>Output:</strong> 104
	</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= piles.length &lt;= 100</code></li>
<li><code>1 &lt;= piles[i] &lt;= 10<sup>4</sup></code></li>
</ul>
</div>

---
# [Solution](solution.md)