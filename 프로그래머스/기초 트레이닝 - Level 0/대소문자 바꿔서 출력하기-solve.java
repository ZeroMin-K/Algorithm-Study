import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        StringBuilder sb = new StringBuilder();
        
        for (char alpha : a.toCharArray()) {
            if (Character.isUpperCase(alpha)) sb.append(Character.toLowerCase(alpha));
            else sb.append(Character.toUpperCase(alpha));
        }
        
        System.out.println(sb.toString());
    }
}