public class fatorial {
    public static void main(String[] args) {
        
        int number = 5;
        int fatorial = 1;

        for(int i = 1;i <= number; i++){
            fatorial = fatorial * i;
            System.out.println(i);
        }
    }
}
