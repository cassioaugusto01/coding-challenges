'''
https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/
3080. Mark Elements on Array by Performing Queries
Medium

You are given a 0-indexed array nums of size n consisting of positive integers.

You are also given a 2D array queries of size m where queries[i] = [indexi, ki].

Initially all elements of the array are unmarked.

You need to apply m queries on the array in order, where on the ith query you do the following:

Mark the element at index indexi if it is not already marked.
Then mark ki unmarked elements in the array with the smallest values. If multiple such elements exist, mark the ones with the smallest indices. And if less than ki unmarked elements exist, then mark all of them.
Return an array answer of size m where answer[i] is the sum of unmarked elements in the array after the ith query.


Example 1:

Input: nums = [1,2,2,1,2,3,1], queries = [[1,2],[3,3],[4,2]]

Output: [8,3,0]

Explanation:

We do the following queries on the array:

Mark the element at index 1, and 2 of the smallest unmarked elements with the smallest indices if they exist, the marked elements now are nums = [1,2,2,1,2,3,1]. The sum of unmarked elements is 2 + 2 + 3 + 1 = 8.
Mark the element at index 3, since it is already marked we skip it. Then we mark 3 of the smallest unmarked elements with the smallest indices, the marked elements now are nums = [1,2,2,1,2,3,1]. The sum of unmarked elements is 3.
Mark the element at index 4, since it is already marked we skip it. Then we mark 2 of the smallest unmarked elements with the smallest indices if they exist, the marked elements now are nums = [1,2,2,1,2,3,1]. The sum of unmarked elements is 0.
Example 2:

Input: nums = [1,4,2,3], queries = [[0,1]]

Output: [7]

Explanation: We do one query which is mark the element at index 0 and mark the smallest element among unmarked elements. The marked elements will be nums = [1,4,2,3], and the sum of unmarked elements is 4 + 3 = 7.

 

Constraints:

n == nums.length
m == queries.length
1 <= m <= n <= 105
1 <= n <= 105
queries[i].length == 2
0 <= indexi, ki <= n - 1
'''

# Separa as "regras de negócio" em baby steps
'''
1 You are given a 0-indexed array nums of size n consisting of positive integers.

2 You are also given a 2D array queries of size m where queries[i] = [indexi, ki].

3 Initially all elements of the array are unmarked.

4 You need to apply m queries on the array in order, where on the ith query you do the following:

4.1 - Mark the element at index indexi if it is not already marked.
4.2 - Then mark ki unmarked elements in the array with the smallest values. 

4.3 - If multiple such elements exist, mark the ones with the smallest indices. And if less than ki unmarked elements exist, then mark all of them.

5 - Return an array answer of size m where answer[i] is the sum of unmarked elements in the array after the ith query.
'''

import heapq

class Solution(object):
    def unmarkedSumArray(self, nums, queries):
        # 1 nums: You are given a 0-indexed array nums of size n consisting of positive integers.
        # 2 queries: You are also given a 2D array queries of size m where queries[i] = [indexi, ki].
        
        # Inicializa as variaveis necessárias para a solução:
        # Inicializa a lista de respostas
        answer = [] 
        
        # 3 Initially all elements of the array are unmarked.
        # Inicializa a lista de elementos marcados como False
        marked = [False] * len(nums) 
        
        # Inicializa o min-heap vazio
        min_heap = [] 
        
        # Calcula a soma total dos elementos no array nums
        total_sum = sum(nums)
        
        # Preenche o min-heap com os elementos do array nums
        for i, num in enumerate(nums):
            heapq.heappush(min_heap, (num, i))

        # 4 You need to apply m queries on the array in order, where on the ith query you do the following:
        
        # Itera sobre as queryes
        for index, k in queries:
            # 4.1 - Mark the element at index indexi if it is not already marked.
            # Marca o elemento no índice index se ainda não estiver marcado
            if not marked[index]:
                total_sum -= nums[index]
                marked[index] = True
                
            #4.2 - Then mark ki unmarked elements in the array with the smallest values. 
            # 4.3 - If multiple such elements exist, mark the ones with the smallest indices. And if less than ki unmarked elements exist, then mark all of them.
            # Marca k elementos não marcados com os menores valores
            while k > 0 and min_heap:
                num, i = heapq.heappop(min_heap)
                if not marked[i]:
                    marked[i] = True
                    total_sum -= num
                    k -= 1
            
            # Adiciona a soma dos elementos não marcados à resposta
            #5.1 - monta retorno: Return an array answer of size m where answer[i] is the sum of unmarked elements in the array after the ith query.
            answer.append(total_sum)
        
        # 5.2 - Return an array answer of size m where answer[i] is the sum of unmarked elements in the array after the ith query.
        return answer
    
# testes unitários (rodar somente na ide)    

import unittest

class TestMarkElements(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1, 2, 2, 1, 2, 3, 1]
        queries = [[1, 2], [3, 3], [4, 2]]
        expected_output = [8, 3, 0]
        actual_output = self.solution.unmarkedSumArray(nums, queries)
        self.assertEqual(actual_output, expected_output)

    def test_example2(self):
        nums = [1, 4, 2, 3]
        queries = [[0, 1]]
        expected_output = [7]
        actual_output = self.solution.unmarkedSumArray(nums, queries)
        self.assertEqual(actual_output, expected_output)

if __name__ == "__main__":
    unittest.main()

    
# explicação do heapq
'''
O módulo heapq em Python fornece funções para trabalhar com filas de prioridade (heaps). Um heap é uma estrutura de dados que mantém seus elementos em uma ordem específica, de forma que o elemento de maior prioridade (ou menor, dependendo do tipo de heap) esteja sempre na raiz do heap. O módulo heapq implementa um heap binário usando uma lista.

Na solução do problema "Mark Elements on Array by Performing Queries", o heapq é usado para manter os elementos do array em ordem crescente, facilitando a seleção dos menores elementos não marcados para serem marcados de acordo com as consultas.

Aqui estão os principais recursos do heapq usados na solução:

heapq.heappush(heap, item):

Adiciona um elemento ao heap.
Na solução, isso é usado para preencher o min-heap com os elementos do array nums.
heapq.heappop(heap):

Remove e retorna o menor elemento do heap.
Na solução, isso é usado para selecionar o menor elemento não marcado do min-heap para ser marcado de acordo com as consultas.
heapq.heapify(x):

Transforma a lista x em um heap em tempo linear.
Embora não seja usado explicitamente na solução, é um recurso útil para transformar uma lista desordenada em um heap.
heapq.nsmallest(n, iterable, key=None):

Retorna os n menores elementos do iterável.
Embora não seja usado diretamente na solução, esse recurso poderia ser útil para selecionar os menores elementos não marcados de forma eficiente.
heapq.heapreplace(heap, item):

Remove e retorna o menor elemento do heap e adiciona o novo elemento ao heap.
Embora não seja usado diretamente na solução, é outro método útil para atualizar o heap após uma marcação.
Esses são alguns dos recursos principais do heapq que são utilizados na solução para manipular o min-heap e facilitar a marcação dos elementos não marcados de acordo com as consultas do problema.
'''