public class solution {
	public static void main(String args[]) {
		System.out.println(reverse_integer(135));
		System.out.println(reverse_integer(-321));
	}

	public static int reverse_integer(int n) {
		int ans=0;
		while(n!=0){
			ans = ans*10 + n%10;
			n /= 10;
		}
		return ans;
	}
}