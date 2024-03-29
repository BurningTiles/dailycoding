# Solution - 28 Jun 2023

---
## [1. Merge Overlapping Intervals](https://workat.tech/problem-solving/practice/merge-overlap-intervals) [(LeetCode)](https://leetcode.com/problems/merge-intervals/) 

### cpp
```cpp
vector<vector<int>> mergeIntervals(vector<vector<int>> &a) {
	sort(a.begin(), a.end());
	vector<vector<int>> ans;
	int start = a[0][0], end = a[0][1];
	for(int i=1; i<a.size(); i++)
		if(a[i][0]<=end) end = max(end, a[i][1]);
		else ans.push_back({start, end}), start = a[i][0], end = a[i][1];
	ans.push_back({start, end});
	return ans;
}
```


---
## [2. Kth Largest Element](https://workat.tech/problem-solving/practice/kth-largest-element) [(LeetCode)](https://leetcode.com/problems/kth-largest-element-in-an-array/) 

### cpp
```cpp
int getKthLargestElement(vector<int> &list, int k) {
	sort(list.rbegin(), list.rend());
	return list[k-1];
}

/*
// Another approach using quick sort pivot selection
int k;

void getmedian( vector<int>& nums ){
	int n = nums.size()-1;
	int start = 0 , end = n;
	int i , j;
	while( start != end ){
		int range = end-start+1;
		int random  = rand()%range + start ;
		swap( nums[random],nums[end] );
		int pivot = nums[end];
		for( i = start , j = end-1; i <= j ;   ){
			if( nums[i] >= pivot ){
				swap(nums[i],nums[j]);
				j--;
			}else{
				i++;
			}
		}

		swap(nums[i],nums[end]);
		// for( int num: nums ){
		//     cout << num << " " ;
		// }
		// cout << endl;

		if( i == k ){
			return;
		}else if( i > k ){
			end = i-1;
		}else{
			start = i+1;
		}
	}
	return;    
}
	
int getKthLargestElement(vector<int>& nums, int kk ) {
	k = nums.size()-kk;
	getmedian(nums);
	return nums[k];
}
*/
```