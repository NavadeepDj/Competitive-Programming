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
	    boolean identity = true;
	    for(int i = 0; i<rows; i++){
	        for (int j =0; j<cols; j++){
	            if (i == j){
	                if (arr[i][j] != 1){
	                identity = false;
	            }}
	            if (i != j){ 
	                if(arr[i][j] != 0){
	                identity = false;
	            }
	        }
	    }}
	    if (identity == true){
	        System.out.println("Iden");
	    }
	    else{
	        System.out.println("Nope");
	    }
	}
}
