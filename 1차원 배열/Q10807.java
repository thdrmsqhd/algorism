import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.Collectors;

public class Q10807{
    public static void main(String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String count = br.readLine();
        String numbers = br.readLine();
        String target = br.readLine();

        String[] numArr = numbers.split(" ");
        System.out.println(
            Arrays.stream(numArr)
                .filter(n ->  n.equals(target))
                .map(n -> Integer.parseInt(n))
                .collect(Collectors.toList())
                .size()
        );

    }
}