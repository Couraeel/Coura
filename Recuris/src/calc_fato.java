public class calc_fato {
    public static void main(String[] args) {
        
        int result = calculo(4);
        System.out.println(result);
    }
    public static int calculo(int n){
        if (n == 0 || n == 1){
            return 1;
        }
        else{
            return n * calculo(n - 1);
        }
    }
}