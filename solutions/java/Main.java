import java.util.Scanner;

public class Main {
    
    // Problem 1
    static void problem1() {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(), b = sc.nextInt();
        System.out.println(a + b);
    }
    
    // Problem 2
    static void problem2() {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
        System.out.println(Math.max(a, Math.max(b, c)));
    }
    
    // Problem 3
    static void problem3() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(n % 2 == 0 ? "Even" : "Odd");
    }
    
    // Problem 4
    static void problem4() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), fact = 1;
        for(int i=1; i<=n; i++) fact *= i;
        System.out.println(fact);
    }
    
    // Problem 5
    static void problem5() {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println(new StringBuilder(s).reverse());
    }
    
    // Problem 6
    static void problem6() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), a=0, b=1;
        for(int i=0; i<n; i++) {
            int temp = a;
            a = b;
            b += temp;
        }
        System.out.println(a);
    }
    
    public static void main(String[] args) {
        if(args.length < 1) System.exit(1);
        
        switch(args[0]) {
            case "1": problem1(); break;
            case "2": problem2(); break;
            case "3": problem3(); break;
            case "4": problem4(); break;
            case "5": problem5(); break;
            case "6": problem6(); break;
        }
    }
}