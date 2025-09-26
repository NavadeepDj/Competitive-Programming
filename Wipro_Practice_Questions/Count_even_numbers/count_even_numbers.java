public class CountEvens {
    public static int countEvens(int a, int b, int c, int d, int e) {
        int[] nums = {a, b, c, d, e};
        int count = 0;
        for (int num : nums) {
            if (num % 2 == 0) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(countEvens(2, 3, 6, 7, 8)); // Output: 3
    }
}
