// Cleaner code and Easily scalable for different currencies

import java.util.Scanner;

public class Minimum_currency_notes {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int amt = sc.nextInt();
        int notes_count = 0;

        int[] denominations = {100, 50, 10, 5, 2, 1};

        for (int note : denominations) {
            if (amt >= note) {
                notes_count += amt / note;
                amt = amt % note;
            }
        }

        System.out.println(notes_count);
    }
}