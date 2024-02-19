import java.util.HashSet;
import java.util.Set;

public class IsUnique {
    
    public static boolean isUnique(String i) {

        Set<Character> hashSet = new HashSet<>();

        for (char c : i.toCharArray()) {
            hashSet.add(c);
        }

        if (hashSet.size() == i.length()){
            return true;
        }
        

        return false;
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
