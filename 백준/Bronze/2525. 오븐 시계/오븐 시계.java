import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        int A = Integer.parseInt(input.split(" ")[0]);
        int B = Integer.parseInt(input.split(" ")[1]);
        int C = Integer.parseInt(br.readLine());
        
        int minuit = (A * 60 + B + C) % 1440; 
        System.out.println(minuit / 60 + " " + minuit % 60); 
  }
 }