import unittest

def isUnique(i):
    if len(set(i)) == len(i):
        return True
    return False








class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(isUnique("aaa"), False)
        self.assertEqual(isUnique("abc"), True)
        
if __name__ == "__main__":
    unittest.main()