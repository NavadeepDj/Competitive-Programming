import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        double total = sc.nextDouble();  // total sum (can be float for accuracy)
        
        // Let’s try to solve: x + 2x + x/2 = total
        // Try all values of x from 1 to total and check which one satisfies the equation
        double x = 0;

        for (double i = 1; i <= total; i++) {
            double sum = i + 2 * i + i / 2; // total on 3 days
            if (Math.abs(sum - total) < 0.001) { // small tolerance for float comparison
                x = i;
                break;
            }
        }

        System.out.println("First Day: " + x);
        System.out.println("Second Day: " + 2 * x);
        System.out.println("Third Day: " + x / 2);
    }
}
