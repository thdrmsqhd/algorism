public class Q46673{

    public static void main(String[] args){
        int n = 1;
        while (n < 100){
            String parseStr = Integer.toString(n);
            String[] strArr = parseStr.split("");
            if(strArr.length>1){
                int minus = 0;
                for(int i = 0 ; i<strArr.length ; i++){
                    minus = n - Integer.parseInt(strArr[i]);
                }
                System.out.println(minus);
            }else{
                if(!(n%2 == 0)){
                    System.out.println(n);
                }
            }
            n++;
        }
    }
    
}