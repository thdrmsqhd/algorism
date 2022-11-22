import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Q5597{
    public static void main(String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> studentList = new ArrayList<Integer>();
        for(int i = 0 ; i< 28; i++){
            studentList.add(Integer.parseInt(br.readLine()));
        }       
        
        // 길이를 30을 만들고
        int[] newArr = new int[31];
        for(int i = 1 ; i<31; i++){
            newArr[i] = i;
        }
        // 길이가 30개인 배열이랑 비교
        List<Integer> newList = Arrays.stream(newArr)
                                    .boxed()
                                    .collect(Collectors.toList());
        
        newList.removeAll(studentList);
        System.out.println(Integer.toString(newList.get(1)));
        System.out.println(Integer.toString(newList.get(newList.size()-1)));
        
    }
}