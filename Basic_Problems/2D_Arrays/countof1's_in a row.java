import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    int rows = sc.nextInt();
	    int cols = sc.nextInt();
	    int arr[][] = new int[rows][cols];
	    for(int i = 0; i<rows; i++){
	        for (int j =0; j<cols; j++){
	            arr[i][j] = sc.nextInt();
	        }
	    }
	    
	   // int num= 1;
	    int k = 0;
	    int count = 0;
	    int arr1[] = new int[rows];
	    for(int i = 0; i<rows; i++){
	        count = 0;
	        for (int j =0; j<cols; j++){
	            if (arr[i][j] == 1){
	                count++;
	            }
	        }
	       // System.out.println(count);
	        arr1[k] = count;
	        k++;
	    }
	    for(int i =0;i<arr1.length;i++){
	    System.out.println("row " + i + " -- --"+arr1[i]);
	   //System.out.println(arr1[i]);
	    }
	    
	}
}
