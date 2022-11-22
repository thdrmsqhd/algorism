import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Q3052{
    public static void main(String[] args) throws IOException{
        
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int subjectCount = Integer.parseInt(br.readLine());
        String scores = br.readLine();

        String[] scoreArr = scores.split(" ");
        int[] sortedArr = Arrays.stream(scoreArr).mapToInt(i -> Integer.parseInt(i)).sorted().toArray();
        int maxScore = sortedArr[sortedArr.length-1];
        //점수/최대값*100
        double average = Arrays.stream(sortedArr)
            .mapToDouble(score -> {
                return ((score/(double)maxScore) * 100);
            })
            .reduce(0, (a,b)-> a+b) / (double)scoreArr.length ;
            
        System.out.println(average);
       
    }
}