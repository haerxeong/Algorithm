import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] firstLine = br.readLine().split(" ");
        int N = Integer.parseInt(firstLine[0]); 
        int S = Integer.parseInt(firstLine[1]); 
        
        int[] li = new int[N];
        String[] secondLine = br.readLine().split(" ");
        for (int i = 0; i < N; i++) {
            li[i] = Integer.parseInt(secondLine[i]);
        }

        int minLen = Integer.MAX_VALUE;
        int partSum = li[0];
        int sum = 0;

        for (int i : li) {
            sum += i;
        }

        if (sum < S) {
            System.out.println(0);
        } else {
            int left = 0, right = 0;
            while (left <= right && right < N) {
                if (partSum >= S) {
                    minLen = Math.min(minLen, right - left + 1);
                    partSum -= li[left];
                    left++;
                } else {
                    if (right + 1 < N) partSum += li[right + 1];
                    right++;
                }
            }
            System.out.println(minLen);
        }
    }
}