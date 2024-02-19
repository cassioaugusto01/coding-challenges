// Write a method to replace all spaces in a string with '%20';

//assumir que a string tem espaço suficiente no final pra suportar os caracteres adicionais

public class URLify {

    static void replaceSpaces(char[] str, int trueLength){

        //1 passagem: contar o numero de espaços
        int spaceCount = 0, index, i = 0;
        for (i = 0;i < trueLength; i++){
            if(str[i] == ' '){
                spaceCount++;
            }
        }

        //2 passagem: Editar a String na ordem inversa substituindo os espaços por %20
        index = trueLength + spaceCount * 2;
        if (trueLength < str.length) str[trueLength] = '\0'; // fim do array
        for (i = trueLength - 1; i >=0; i--){
            if (str[i] == ' '){
                str[index - 1] = '0';
                str[index - 2] = '2';
                str[index - 3] = '%';
                index = index -3;
            } else {
                str[index - 1] = str[i];
                index--;
            }
        }
    }
    public static void main(String[] args) {

        String s = "Mr John Smith      ";
        char[] s_array = s.toCharArray();
        replaceSpaces(s_array,13);
        System.out.println(s_array);
    }
}
