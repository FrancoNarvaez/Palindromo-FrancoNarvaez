import unittest

def palindromo (word):
    normal_word = word.lower().replace(' ','')
    reverse_word = normal_word[::-1]

    if normal_word == reverse_word:
        return True
    else:
        return False

class TestPalindromo(unittest.TestCase):
    def test1_condition_happy(self):
        self.assertTrue(palindromo('Reconocer'))
    def test2_condition_happy(self):
        self.assertTrue(palindromo('amor a Roma'))
    def test3_condition_happy(self):
        self.assertTrue(palindromo('Sometemos'))
    def test4_condition_happy(self):
        self.assertTrue(palindromo('neuquen'))
    def test5_condition_happy(self):
        self.assertTrue(palindromo('121'))
    def test6_condicion_happy(self):
        self.assertTrue(palindromo('Anita lava la       tina'))
    def test7_condition_sad(self):
        self.assertFalse(palindromo('Palindromo'))
    def test8_condition_sad(self):
        self.assertFalse(palindromo('Valorant'))
    def test9_condition_sad(self):
        self.assertFalse(palindromo('Que pasa en casa'))
    def test10_condition_sad(self):
        self.assertFalse(palindromo('1234'))
if __name__ == '__main__':
    unittest.main()