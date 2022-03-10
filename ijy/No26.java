import java.util.Scanner;

public class No26 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);

        String str = sc.next();
        
        String[] time = str.split(":");

        System.out.println(time[1]);

        sc.close();
    };
}
