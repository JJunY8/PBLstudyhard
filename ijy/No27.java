import java.util.Scanner;

public class No27 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);

        String str = sc.next();
        
        String[] time = str.split("\\.");

        System.out.printf(String.format("%02s",time[2])+"-"+String.format("%02s",time[1])+"-"+String.format("%04s",time[0]));

        sc.close();
    };
}
