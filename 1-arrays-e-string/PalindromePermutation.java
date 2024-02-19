/*
 * Palindrome Permutation: Dada uma string, escreva uma função para
 * verificar se é a permutação de um palindromo.
 * input: Tact Coa
 * output: True (permutations: "taco cat", "atco cta", etc)
 * 
 * solução:
  *  se tiver 0 ou 1 caracteres que não se repete e todos os outros forem par, retorna true
  * usar hash table pra contar quantas vezes cada caractere aparece
  * iterar no hash table pra ver se não tem mais de um caractere em quantidade impar
  */
public class PalindromePermutation {
    static boolean isPermutationOfPalindrome(String phrase) {
        int[] table = buildCharFrequencyTable(phrase);
        return checkMaxOneOdd(table);
    }

    //verifica se não tem mais de um caractere em quantidade impar
    static boolean checkMaxOneOdd(int[] table){
        boolean foundOdd = false;
        for (int count : table){
            if (count % 2 == 1) {
                if (foundOdd) {
                    return false;
                }
                foundOdd = true;
            }
        }
        return true;
    }

    // mapeia cada caractere a um numero
    static int getCharNumber(Character c){
        int a = Character.getNumericValue('a');
        int z = Character.getNumericValue('z');
        int val = Character.getNumericValue(c);
        if (a <= val && val <= z){
            return val -a;
        }
        return -1;
    }

    //conta quantas vezes cada caractere aparece
    static int[] buildCharFrequencyTable(String phrase) {
        int[] table = new int[Character.getNumericValue('z') - Character.getNumericValue('a') + 1];
        for (char c : phrase.toCharArray()){
            int x = getCharNumber(c);
            if (x != -1) {
                table[x]++;
            }
        }
        return table;
    }

    public static void main(String[] args){

        Boolean saida = isPermutationOfPalindrome("tyaco cat");
        if (saida == true){
            System.out.println("È permutação de um palindromo");
        } else {
            System.out.println("Não È permutação de um palindromo");
        }
        
    }
}