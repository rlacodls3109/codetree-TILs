import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); //개발자 수
        int K = sc.nextInt(); //최대 전염횟수
        int P = sc.nextInt(); //첫 감염자
        int T = sc.nextInt(); //진행 횟수

        int[] infected = new int[N]; //감염여부
        infected[P-1] = 1;
        int[] con = new int[N];      //전염횟수

        //입력값 받기
        int[][] inputs = new int[T][3];
        for(int i=0; i<T; i++){
            for(int j=0; j<3; j++){
                inputs[i][j] = sc.nextInt();
            }
        }
        //입력값 정렬
        for(int i=0; i<T; i++){
            Arrays.sort( inputs, (a, b) -> Integer.compare(a[0], b[0]) ); //첫번째 열 기준
        }

        
        for(int i=0; i<T; i++){
            int x = inputs[i][1]-1;
            int y = inputs[i][2]-1;
            //x가 감염자일때 -> x의 전염횟수 증가, y가 전염자됨
            if(infected[x]==1 && con[x] < K){
                con[x]++;
                infected[y]=1;
            }
            //y가 감염자일때 -> y의 전염횟수 증가, x가 전염자됨
            if(infected[y]==1 && con[y] < K){
                con[y]++;
                infected[x]=1;
            }
        }

        for(int i=0; i<N; i++) System.out.print(infected[i]);



    }
}