import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        int n;

        Scanner sc = new Scanner(System.in);

        System.out.println("Hello"); // 출력하기01
        System.out.println("Hello World"); // 출력하기 02
        System.out.println("Hello\nWorld"); // 출력하기 03
        System.out.println("\'Hello\'"); // 출력하기 04
        System.out.println("\"Hello World\""); // 출력하기 05
        System.out.println("\"!@#$%^&*()\""); // 출력하기 06
        System.out.println("\"C:\\Download\\hello.cpp\""); // 출력하기 07
        System.out.println("┌┬┐"); 
        System.out.println("├┼┤");
        System.out.println("└┴┘");
        System.out.println("\u250C\u252C\u2510\n");
        System.out.println("\u251C\u253C\u2524\n");
        System.out.println("\u2514\u2534\u2518\n");// 출력하기 08

        n = sc.nextInt();
        System.out.println(n);//정수 1개 입력받아 그대로 출력하기
    }
}
