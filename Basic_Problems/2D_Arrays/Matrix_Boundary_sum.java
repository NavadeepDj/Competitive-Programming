import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
		int m = sc.nextInt();
				int n = sc.nextInt();

		int arr[][] = new int[m][n];
		for (int i =0; i< m; i++){
		    for (int j =0; j<n; j++){
		        arr[i][j] = sc.nextInt();
		    }
		}
		int sum = 0;
		for (int i =0; i< m; i++){
		    for (int j =0; j<n; j++){
		        if (i ==0 || i ==m-1){
		        sum += arr[i][j];
		    }
		    if (i !=  0 && i != m-1){
		        if (j == 0 || j == m-1){
		        sum += arr[i][j];
		    }
		    }
		}}
		System.out.println(sum);
	}}
// 		00 01 02
// 		10    12
// 		20 21 22
