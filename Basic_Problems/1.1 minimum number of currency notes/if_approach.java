import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
		int amt = sc.nextInt();
		int notes_count = 0;
		if (amt >= 100){
		    notes_count += amt / 100;
		    amt = amt % 100;
		}
		if (amt >= 50){
		    notes_count += amt / 50;
		    amt = amt % 50;
		}
		if (amt >= 10){
		    notes_count += amt / 10;
		    amt = amt % 10;
		}
		if (amt >= 5){
		    notes_count += amt / 5;
		    amt = amt % 5;
		}
		if (amt >= 2){
		    notes_count += amt / 2;
		    amt = amt % 2;
		}
		if (amt >= 1){
		    notes_count += amt / 1;
		    amt = amt % 1;
		}
		System.out.println(notes_count);
	}
}
