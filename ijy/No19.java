import java.util.Scanner;

public class No19 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);

        String str = sc.next();

        String[] n = str.split("\\.");

        System.out.println(String.format("%s.%02s.%02s",n[0],n[1],n[2]));

        sc.close();
    };
}
