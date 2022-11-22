import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class Q1065{

    public static void main(String[] args) throws NumberFormatException, IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println(countHansu(Integer.parseInt(br.readLine())));
    }

    public static int countHansu(int untilNumber){
        if(untilNumber == 1) return 1;
        HashSet<Integer> resultSet = new HashSet<Integer>(); 
        for(int i = -9 ; i <= 9 ; i ++){
            for(int j = 1; j <= untilNumber; j++ ){
                int result = getHansu(j, i);
                if(result > 0){
                    // System.out.print(result);
                    // System.out.print(" ");
                    resultSet.add(result);
                }
            }
            // System.out.println();
        }
    
        // System.out.println(resultSet.size());
        return resultSet.size();
    }

    public static int getHansu(int number, int gap){
        int saveNumber = new Integer(number).intValue();
        int copyNumber = new Integer(number).intValue();
        List<Integer> numList = new ArrayList<Integer>();
        while(copyNumber > 0){
            numList.add(copyNumber%10);
            copyNumber = copyNumber/10;
        }

        int gapValue = new Integer(gap).intValue();
        boolean check = true;
        if(numList.size() > 1){
            for(int i = 0 ; i < numList.size() -1 ; i++){
                if(!(numList.get(i) - numList.get(i+1) == gapValue)){
                    check = false;
                }
            }
        }
        if(check){
            return saveNumber;
        }else{
            return 0;
        }
    }
}