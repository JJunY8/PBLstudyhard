import java.util.Scanner;

public class No23 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);

        String str = sc.next();
        String[] n=str.split("\\.");
        System.out.printf("%s\n%s",n[0],n[1]);

        sc.close();
    };
}
