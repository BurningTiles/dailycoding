public class solution {
	public static void main(String args[]) {
		String s1[] = {"helloworld", "hellokitty", "hell"};
		String s2[] = {"daily", "interview", "pro"};
		System.out.println(longest_common_prefix(s1));
		System.out.println(longest_common_prefix(s2));
	}

	public static String longest_common_prefix(String s[]) {
		if(s.length==0) return "";
		String prefix = s[0];
		for(int i=1; i<s.length; i++){
			int j=0;
			while(j<s[i].length() && j<prefix.length() && s[i].charAt(j)==prefix.charAt(j))
				j++;
			if(j==0) return "";
			prefix = prefix.substring(0, j);
		}
		return prefix;
	}
}