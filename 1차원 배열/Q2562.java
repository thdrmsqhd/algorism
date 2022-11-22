import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;

public class Q2562{
    public static void main(String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // String count = br.readLine();
        // String numbers = br.readLine();
        // String target = br.readLine();

        
        String input1 = br.readLine();
        String input2 = br.readLine();
        String input3 = br.readLine();
        String input4 = br.readLine();
        String input5 = br.readLine();
        String input6 = br.readLine();
        String input7 = br.readLine();
        String input8 = br.readLine();
        String input9 = br.readLine();
        
        HashMap<String,String> numberMap = new HashMap<String,String>();
        numberMap.put(input1, "1");
        numberMap.put(input2, "2");
        numberMap.put(input3, "3");
        numberMap.put(input4, "4");
        numberMap.put(input5, "5");
        numberMap.put(input6, "6");
        numberMap.put(input7, "7");
        numberMap.put(input8, "8");
        numberMap.put(input9, "9");
        
        List<String> numberList = new ArrayList<String>();
        numberList.add(input1);
        numberList.add(input2);
        numberList.add(input3);
        numberList.add(input4);
        numberList.add(input5);
        numberList.add(input6);
        numberList.add(input7);
        numberList.add(input8);
        numberList.add(input9);

        String ind = Integer.toString(
            numberList.stream()
                .map(i -> Integer.parseInt(i))
                .sorted()
                .max(Comparator.comparing(x -> x))
                .get()
        );
        System.out.println(ind);
        System.out.println(numberMap.get(ind));
    }
}