import java.util.Scanner;

public class test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] result = new int[N+1];
        int[] prices = new int[N+1];
        for (int i = 1; i <= N; i++) {
            prices[i] = sc.nextInt();
        }
        for (int i=1;i <= N; i++) {
            for (int j=1;j <= i; j++) {
                result[i] = Math.max(prices[j] + result[i-j], result[i]);
            }
        }
        System.out.println(result[N]);
        sc.close();
    }
}
