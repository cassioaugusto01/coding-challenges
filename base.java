public class base {
    
    public static int soma(int a, int b) {
        return a + b;
    }


    public static void main(String[] args) {
        if (soma(1,1) == 2) {
            System.out.println("Teste 1 passou");
        } else {
            System.out.println("Teste 1 falhou");
        }
    }
}
