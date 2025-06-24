/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int arr[] = new int[n];
		for (int i =0; i< n; arr[i++] = sc.nextInt());
		int index = 0;
		int max = 0;
		int maxi = 0;
		int arr1[] = new int[n];
		int k =0;
		while (max != arr[n-1]){
		max = 0;
// 		System.out.println("MAXI"+maxi);
		for (int i = maxi+1; i < n; i++){
		    		// System.out.println("MAXI"+maxi);
		    if (arr[i] > max){
		        max = arr[i];
		        maxi = i; 
		    }
// 		    System.out.println("Max"+max);
// 		System.out.println("maxi"+maxi);
		}
// 		System.out.println("Max"+max);
// 		System.out.println("maxi"+maxi);
		   arr1[k] = max;
		    k++; 
// 		System.out.println("\n");
		}
		int sum =0;
		for (int i = 0; i < arr1.length; i++){
		    sum += arr1[i];
		}
		
		System.out.println(sum);
		
	}
}
