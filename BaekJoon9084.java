import java.util.Scanner;

public class test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        while (T-- > 0) {
            // 초기화
            int N = sc.nextInt();
            int[] price = new int[N];
            for (int i=0; i < N; i++) {
                price[i] = sc.nextInt();
            }
            int goal = sc.nextInt();

            // 1 ~ goal 원을 만들기 위한 모든 방법의 수의 배열
            int[] result = new int[goal + 1];

            result[0] = 1;
            for (int i=1; i<= N; i++) {
                for (int j = price[i-1]; j <= goal; j++) {
                    result[j] += result[j - price[i-1]];
                }
            }

            System.out.println(result[goal]);
        }

        sc.close();
    }
}
