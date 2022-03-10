import java.util.Scanner;

public class No18 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);

        String str = sc.next();

        String[] time = str.split(":");

        System.out.printf(String.format("%s:%s",time[0],time[1]));
        sc.close();
    };
}
