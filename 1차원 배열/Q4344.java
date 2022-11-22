import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Q4344{
    public static void main(String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCaseCount = Integer.parseInt(br.readLine());
        String[] testCases = new String[testCaseCount];
        for(int i = 0 ; i<testCaseCount; i++){
            testCases[i] = br.readLine();
        }
        
        // int testCaseCount = 5;
        // String[] testCases = new String[testCaseCount];
        // testCases[0] = "5 50 50 70 80 100";
        // testCases[1] = "7 100 95 90 80 70 60 50";
        // testCases[2] = "3 70 90 80";
        // testCases[3] = "3 70 90 81";
        // testCases[4] = "9 100 99 98 97 96 95 94 93 91";
        
        
        Arrays.stream(testCases).forEach(testCase ->{
            String[] splitStr = testCase.split(" ");
            
            int[] splitData = Arrays.stream(splitStr)
                .mapToInt(i -> Integer.parseInt(i))
                .toArray();
            
            int studentCount = splitData[0];

            // 평균 구하기
            int sum = 0;
            for(int i = 1 ; i<splitData.length ; i++){
                sum += splitData[i];
            }

            double avarage = sum/(double)studentCount;
            // 평균이 넘는 사람 찾기
            int overAvarageCount = 0;
            for(int i = 1 ; i<splitData.length ; i++){
                if(avarage < splitData[i]){
                    overAvarageCount++;
                }
            }
            double avarageOverPer = ((double)overAvarageCount/studentCount) * 100;
           
            System.out.println(String.format("%1$,.3f",avarageOverPer)+"%");
        });
    }
}