import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String num;
        if (n % 2 == 0) {
            num = "even";
        } else {
            num = "odd";
        }
        System.out.println(n + " is " + num);
    }
}