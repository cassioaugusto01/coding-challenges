import java.util.HashSet;
import java.util.Set;

public class IsUnique2 {
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    
    public static boolean isUnique(String str) {

        // string ASCII tem 128 caracteres possíveis
        // se > 128 tem caractere repetido
        if (str.length() > 128) return false;

        // charset com todos os caractes ASCII
        // flag que indica se o caractere se repete
        boolean[] char_set = new boolean[128];

        for (int i = 0; i < str.length(); i++){
            int valorAtual = str.charAt(i);

            //se esse caractere já foi visto na string
                //retorna false
            if (char_set[valorAtual]) {
                return false;
            }
            char_set[valorAtual] = true;
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
