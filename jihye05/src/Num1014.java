package CodeUp.src;
import java.util.Scanner;

public class Num1014{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        
        char num1, num2;
        String str;
        str = in.nextLine();

        num1 = str.charAt(0);
        num2 = str.charAt(2);

        System.out.println(num2);
        System.out.println(num1);

        in.close();
    }
}
