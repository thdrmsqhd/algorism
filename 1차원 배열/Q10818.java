import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Q10818{
    public static void main(String[] args) throws IOException{
        
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // String count = br.readLine();
        // String numbers = br.readLine();
        // String target = br.readLine();

        String count = "5";
        String numbers = "20 10 35 30 7";

        String[] numArr = numbers.split(" ");
        
        List<String> result = Arrays.asList(numArr).stream()
                .map(n -> Integer.parseInt(n))
                .sorted()
                .map(n -> Integer.toString(n))
                .collect(Collectors.toList());
        
        System.out.println(result.get(0) + " " + result.get(result.size() - 1));
    }
}