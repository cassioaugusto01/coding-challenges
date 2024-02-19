/*
 * 1.5 One Away
 * tem 3 tipos de edição que podem ser feitos em strings:
 * inserir, remover ou substituir caractere.
 * Dadas 2 string, escreva uma função para verificar se são um exemplo de uma edição
 * (ou zero edições)
 */
public class OneAway {
    boolean oneEditAway(String first, String second){
        if (first.length() == second.length()){
            return oneEditReplace(first, second);
        } else if (first.length() + 1 == second.length()){
            return oneEditInsert(first, second);
        } else if (first.length() - 1 == second.length()) {
            return oneEditInsert(second, first);
        }
        return false;
    }

    boolean oneEditReplace(String s1, String s2){
        boolean foundDifference = false;
        for (int i = 0; i < s1.length(); i++){
            if (s1.charAt(i) != s2.charAt(i)) {
                if (foundDifference){
                    return false;
                }
                foundDifference = true;
            }
        }
        return true;
    }

    //ve se pode inserir um caractere em s1 para ele se transformar no s2
    static boolean oneEditInsert(String s1, String s2){
        int index1 = 0;
        int index2 = 0;
        while (index2 < s2.length() && index1 < s1.length()){
            if (s1.charAt(index1) != s2.charAt(index2)) {
                if (index1 != index2){
                    return false;
                }
                index2++;
            } else{
                index1++;
                index2++;
            }
        }
        return true;
    }

    public static void main(String[] args){
        boolean retorno = oneEditInsert("ple", "zxw");
        if (retorno == true){
            System.out.println("é um one edit insert");
        } else{
            System.out.println("não é um one edit insert");
        }
    }
    
}
