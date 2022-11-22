import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ReadInput{
    public static void main(String[] args) throws IOException{
        
        // 버퍼리더
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String a = br.readLine();
		br.close();
    }
}