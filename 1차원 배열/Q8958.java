import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Q8958{
    public static void main(String[] args) throws IOException{
        
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCaseCount = Integer.parseInt(br.readLine());
        List<String> testCases = new ArrayList<String>();
        for(int i = 0; i<testCaseCount; i++){
            testCases.add(br.readLine());
        }
        // int testCaseCount = 5;
        // List<String> testCases = Arrays.asList(
        //     "OOXXOXXOOO"
        //     ,"OOXXOOXXOO"
        //     ,"OXOXOXOXOXOXOX"
        //     ,"OOOOOOOOOO"
        //     ,"OOOOXOOOOXOOOOX"
        // );
        // O의점수는 누적
        // X가 중간에 끼면 누적 초기화
        List<Integer> result = testCases.stream().map(testCase -> {
            String[] checkStatus = testCase.split("");
            int accumulator = 0;
            int totalScore = 0;
            for(int i = 0 ; i<checkStatus.length; i++){
                if(checkStatus[i].equals("O")){
                    //누적 점수 처리
                    accumulator += 1;
                    totalScore += accumulator;
                }

                if(checkStatus[i].equals("X")){
                    //0점처리
                    accumulator = 0;
                }
            }
            return totalScore;
        }).collect(Collectors.toList());

        result.forEach(n -> System.out.println(n));
    }
}