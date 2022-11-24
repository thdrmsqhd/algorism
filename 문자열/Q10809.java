package 문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map.Entry;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // String input = br.readLine();
        String input = "aba";
        String[] strArr = input.split("");
        HashMap<String, Integer> alpaMap = new HashMap<String, Integer>();
        String[] alpaArr = { "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "s",
                "t", "u", "v", "w", "x", "y", "z" };
        Arrays.stream(alpaArr).forEach(a -> alpaMap.put(a, -1));

        for (int i = 0; i < strArr.length; i++) {
            if (alpaMap.get(strArr[i]) == -1) {
                alpaMap.put(strArr[i], i);
            }
        }

        for (Entry<String, Integer> alpa : alpaMap.entrySet()) {
            System.out.print(alpa.getValue() + " ");
        }
    }
}