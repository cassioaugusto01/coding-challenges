import unittest

def soma(numero1, numero2):
    return numero1 + numero2



class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(soma(1,1), 2)
        
if __name__ == "__main__":
    unittest.main()