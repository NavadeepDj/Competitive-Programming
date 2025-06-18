import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
		int total = sc.nextInt();
		int x;
// 		(x + 2x + x/2) = total;
        // total = x + 2*x + (x/2);
        x = (total*2)/7;
		System.out.println("First Day" + x);
		System.out.println("seond Day" + 2*x);
		System.out.println("thrid Day" + x/2);
	}
}
