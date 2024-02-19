import java.util.HashSet;
import java.util.Set;

public class IsUniqueBitVector {

    
    public static boolean isUnique(String str) {
        int checker = 0;
        for (int i = 0; i < str.length(); i++){
            int valorAtual = str.charAt(i) - 'a';
            if ((checker & (1 << valorAtual)) > 0) {
                return false;
            }
            checker |= (1 << valorAtual);
        }

        
        return true;

    }



    public static void main(String[] args) {
        if (isUnique("aaa") == false) {
            System.out.println("Teste 1 passou");
        } else {
            System.out.println("Teste 1 falhou");
        }

        if (isUnique("abc") == true) {
            System.out.println("Teste 2 passou");
        } else {
            System.out.println("Teste 2 falhou");
        }
    }
}
