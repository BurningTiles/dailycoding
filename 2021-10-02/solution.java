public class solution {
	public static void main(String args[]) {
		System.out.println(sum_binary("11101", "1011"));
	}

	public static String sum_binary(String n1, String n2) {
		String ans = "";
		int i=n1.length()-1, j=n2.length()-1, sum=0;
		while(i>=0 || j>=0 || sum>0){
			sum += i>=0 ? n1.charAt(i)-'0' : 0;
			sum += j>=0 ? n2.charAt(j)-'0' : 0;
			ans = (char)(sum%2+'0') + ans;
			sum /= 2;
			--i;
			--j;
		}
		return ans;
	}
}