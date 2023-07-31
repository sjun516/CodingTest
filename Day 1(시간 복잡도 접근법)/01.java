// [필수] 구간의 합들

import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        int[] array = new int[a];
        for(int i =0; i < a; i++) {
            array[i] = sc.nextInt();
        }

        int cnt = 0;
        for(int i =0; i < a; i++) {
            int sum = 0;
            for(int j = i; j < a; j++) {
                sum += array[j];
                if(sum == b) {
                    cnt++;
					break;
                }
            }
        }

        System.out.println(cnt);
    }
}