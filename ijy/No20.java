import java.util.Scanner;

public class No20 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);

        String str = sc.next();

        String[] n = str.split("-");

        System.out.printf("%s%s",n[0],n[1]);

        sc.close();
    };
}
