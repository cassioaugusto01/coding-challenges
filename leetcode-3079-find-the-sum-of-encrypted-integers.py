'''
You are given an integer array nums containing positive integers. We define a function encrypt such that encrypt(x) replaces every digit in x with the largest digit in x. For example, encrypt(523) = 555 and encrypt(213) = 333.

Return the sum of encrypted elements.
------------------------------------------
step by step:

1 - You are given an integer array nums containing positive integers. 
2 - We define a function encrypt such that encrypt(x) replaces every digit in x with the largest digit in x. For example, encrypt(523) = 555 and encrypt(213) = 333.

3 - Return the sum of encrypted elements.
------------------------------------------
Estratégia: 
object calisthenics:
um passo por linha

'''
# TDD
# 1 - definir testes unitários com base nos exemplos do enunciado
# 2 - Fazer passar nos testes
# 3 - categorizar o problema
# 4 - resolver o problema

'''
Categorização do problema:

A partir do texto do enunciado do problema, podemos identificar várias pistas que nos levam a determinar a categoria do problema como "array manipulation and digit manipulation"

1 - O problema envolve manipulação de elementos em uma lista (integer array nums), indicando uma possível categoria de manipulação de arrays.

2 - A função encrypt(x) é definida para substituir cada dígito em x pelo maior dígito em x, o que sugere uma manipulação dos dígitos dos números.

3 - O objetivo é retornar a soma dos elementos encriptados, o que implica uma operação de soma sobre os elementos manipulados.

o problema requer a manipulação de arrays para processar os números dados e a manipulação dos dígitos desses números para calcular a soma dos elementos encriptados. Portanto:
'''
# categoria do problema: array manipulation and digit manipulation


# refatorações com base no clean code, refactoring e object calisthenics:
    # refatoração 1: extrair a função encrypt
    # refatoração 2: um passo por linha
 
class Solution:
    def sumOfEncryptedInt(self, nums: list[int]) -> int:
        # 1 - You are given an integer array nums containing positive integers.
        
        # Initialize a variable to store the total sum
        total_sum = 0
        
        # Iterate through each integer in the input array
        # Repeat steps for all integers in nums.
        for num in nums:
            
            # Convert the integer to a string for digit manipulation
            str_num = str(num)
            
            # Find the largest digit in the string
            max_digit = max(str_num)
            
            # 2 - Encrypt the integer
            encrypted_num = encrypt(max_digit, str_num)
            
            # Add the encrypted integer to the total sum
            total_sum += encrypted_num
        
        # 3 - Return the sum of encrypted elements.
        return total_sum

# 2 - Encrypt the integer by replacing every digit with the largest digit
def encrypt(max_digit, str_num):
    # Calculate the length of the string representation of the number
    length = len(str_num)
    
    # Create a string containing the largest digit repeated 'length' times
    encrypted_str = max_digit * length
    
    # Convert the encrypted string back to an integer
    encrypted_num = int(encrypted_str)
    
    # Return the encrypted integer
    return encrypted_num


import unittest

class TestSumOfEncryptedInt(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1, 2, 3]
        expected_output = 6
        self.assertEqual(self.solution.sumOfEncryptedInt(nums), expected_output)

    def test_example2(self):
        nums = [10, 21, 31]
        expected_output = 66
        self.assertEqual(self.solution.sumOfEncryptedInt(nums), expected_output)

import unittest

class TestEncrypt(unittest.TestCase):
    def setUp(self):
        self.max_digit = '5'  # Maior dígito para encriptação

    def test_encrypt_single_digit(self):
        str_num = '7'
        expected_output = 5
        actual_output = encrypt(self.max_digit, str_num)
        self.assertEqual(actual_output, expected_output)

    def test_encrypt_multiple_digits(self):
        str_num = '123'
        expected_output = 555
        actual_output = encrypt(self.max_digit, str_num)
        self.assertEqual(actual_output, expected_output)
    '''
    def test_encrypt_zero(self):
        str_num = '0'
        expected_output = 0
        actual_output = encrypt(self.max_digit, str_num)
        self.assertEqual(actual_output, expected_output)
    '''

if __name__ == "__main__":
    unittest.main()
