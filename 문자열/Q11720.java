package 문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Q11720 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String len = br.readLine();
        String num = br.readLine();
        String[] numArr = num.split("");
        int result = 0;
        for (int i = 0; i < numArr.length; i++) {
            result = result + Integer.parseInt(numArr[i]);
        }
        System.out.println(result);
    }
}