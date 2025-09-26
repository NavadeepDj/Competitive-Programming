public class LastDigitDemo {
    
    // Method 1: Using Math.abs()
    static int lastDigit(int num) {
        return Math.abs(num) % 10;
    }

    // Method 2: Without abs(), manual fix
    static int lastDigitNoAbs(int num) {
        int rem = num % 10; // In Java, remainder has same sign as dividend
        return (rem < 0) ? -rem : rem; 
    }

    public static void main(String[] args) {
        int[] testCases = {123, -123, -10, 456, -19};

        System.out.println("Java Results:");
        for (int n : testCases) {
            System.out.printf("%d -> abs method: %d, no-abs method: %d%n",
                    n, lastDigit(n), lastDigitNoAbs(n));
        }
    }
}
