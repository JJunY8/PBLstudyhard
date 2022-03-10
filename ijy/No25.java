import java.util.Scanner;

public class No25 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);

        int str = sc.nextInt();
        int one = str/10000;
        int two = (str%10000)/1000;
        int three = ((str%10000)%1000)/100;
        int four = (((str%10000)%1000)%100)/10;
        int five = str%10;

        System.out.printf("["+one*10000+"]");
        System.out.printf("["+two*1000+"]");
        System.out.printf("["+three*100+"]");
        System.out.printf("["+four*10+"]");
        System.out.printf("["+five+"]");
        
        sc.close();
    };
}
