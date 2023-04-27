public class solution {
	public static void main(String args[]) {
		System.out.println(integer_to_roman(1000));
		System.out.println(integer_to_roman(48));
		System.out.println(integer_to_roman(444));
	}

	public static String integer_to_roman(int n) {
		String ans="";
		final int val[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
		final String rom[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
		for(int i=0; i<13; i++)
			while(n>=val[i]){
				n -= val[i];
				ans += rom[i];
			}
		return ans;
	}
}