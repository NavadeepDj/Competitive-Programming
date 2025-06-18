    // Cleaner code and Easily scalable for different currencies

    import java.util.Scanner;

    public class calculator {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            char operator = sc.next().charAt(0);
            int a = sc.nextInt();
            int b = sc.nextInt();


            switch (operator){
                case '*': 
                System.out.println("operator: " + operator);
                System.out.printf("%d + %s + %d", a, operator, b);
                break;
                case '+':
                System.out.println(a + operator+b);
                System.out.println(a+b);
                break;
            
            }

        }
    }
