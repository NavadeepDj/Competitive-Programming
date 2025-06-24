import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];
        for (int i =0; i< n;arr[i++] = sc.nextInt());
        int j =0;
        for (int i =n-1; i >= 0; i--){
            if (arr[i] != 0){
                int temp = arr[n-j-1];
                arr[n-j-1] = arr[i];
                arr[i] = temp;
                j++;
            }
        }
        
        for (int i =0; i< n;i++){
            System.out.println("Array"+arr[i]);
        }
	}
}

// [0, 0 , 1, 2, 3, 0, 0]
