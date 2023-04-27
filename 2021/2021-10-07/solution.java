import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class solution {
	public static void main(String args[]) {
		int a[] = {1, 1, -1, 0, -2, 1, -1};
		int b[] = {3, 0, 1, -5, 4, 0, -1};
		int c[] = {0, 0, 0, 0, 0};
		System.out.println(Arrays.deepToString(fourSum(a, 0)));
		System.out.println(Arrays.deepToString(fourSum(b, 1)));
		System.out.println(Arrays.deepToString(fourSum(c, 0)));
	}

	public static int[][] fourSum(int nums[], int target) {
		List <int[]> ans = new ArrayList<int[]>();
		Arrays.sort(nums);
		for(int i=0; i<nums.length; i++){
			if(i>0 && nums[i]==nums[i-1]) continue;
			for(int j=i+1; j<nums.length; j++){
				if(j>i+1 && nums[j]==nums[j-1]) continue;
				int left=j+1, right=nums.length-1;
				int t = nums[i]+nums[j];
				while(left<right){
					if(left>j+1 && nums[left]==nums[left-1]){
						left++;
						continue;
					}
					int tmp = t+nums[left]+nums[right];
					if(tmp==target){
						int oneSolution[] = {nums[i], nums[j], nums[left], nums[right]};
						ans.add(oneSolution);
						++left;
					}
					else if(tmp<target) ++left;
					else --right;
				}
			}
		}
		int a[][] = new int[ans.size()][];
		for(int i=0; i<a.length; i++)
			a[i] = ans.get(i);
		return a;
	}
}