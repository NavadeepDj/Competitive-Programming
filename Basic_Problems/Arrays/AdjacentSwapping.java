import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int arr[] = new int[n];
		for (int i =0; i< n; arr[i++] = sc.nextInt());
		for (int i =0; i<n; i=i+2) {
			int temp = arr[i];
			arr[i] = arr[i+1];
			arr[i+1] = temp;
		}
		for (int i =0; i< n; i++) {
			System.out.print(arr[i]+" ");
		}
	}
}
// [1,2,3,4,5,6] -> [2,1,4,3,6,5]
