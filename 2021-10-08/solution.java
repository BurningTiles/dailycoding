import java.util.ArrayList;
import java.util.List;

public class solution {
	public static void main(String args[]) {
		System.out.println(generate_brackets(1));
		System.out.println(generate_brackets(3));
	}

	public static List<String> generate_brackets(int n) {
        List<String> ans = new ArrayList<String>();
        if (n == 0) {
            ans.add("");
        } else {
            for (int c = 0; c < n; ++c)
                for (String left: generate_brackets(c))
                    for (String right: generate_brackets(n-1-c))
                        ans.add("(" + left + ")" + right);
        }
        return ans;
    }
}