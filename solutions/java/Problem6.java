import java.util.Scanner;
public class Problem6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), a=0, b=1;
        for(int i=0; i<n; i++) {
            int temp = a;
            a = b;
            b += temp;
        }
        System.out.println(a);
    }
}