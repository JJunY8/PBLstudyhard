import java.util.Scanner;

public class No14 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);

        char x = sc.next().charAt(0);
        char y = sc.next().charAt(0);

        System.out.printf("%c %c",y,x);
        sc.close();
    };
}
