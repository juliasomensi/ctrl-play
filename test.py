import unittest

# def soma(a,b):
#     return a + b 

# class testSoma(unittest.TestCase):

#     def testSomaPositivos(self):
#         self.assertEqual(soma(2,3), 5)
#     def testSomaNegativos(self):
#         self.assertEqual(soma(-2,-3), -5)
#     def testSomaZero(self):
#         self.assertEqual(soma(0,0), 0)

# if __name__ == '__main__':
#     unittest.main()

# def dividir(a,b):
#     if b == 0:
#         raise ValueError("divisão por 0")
#     else:
#         return a/b
# class testDividir(unittest.TestCase):
        
#     def testDivisaoPorZero(self):
#         with self.assertRaises(ValueError):dividir(10,0)
# if __name__ == '__main__':
#             unittest.main()

class calculadora:
    def __init__(self):
        self.resultado = 0 

    def soma(self, a,b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b 

    def divisao(self, a, b):
        if b == 0:
            raise ValueError("divisão por 0")
        else:
            return a/b

class testCalculadora(unittest.TestCase):

    def setUp(self):
        self.C = calculadora()
    def testSoma(self):
        self.assertEqual(self.C.soma(5,3), 8)
    def testSubtracao(self):
        self.assertEqual(self.C.subtracao(9,6), 3)
    def testMultiplicacao(self):
        self.assertEqual(self.C.multiplicacao(8,3), 24)
    def testDivisao(self):
        self.assertEqual(self.C.divisao(8,4), 2)
    def testDivisaoPorZero(self):
        with self.assertRaises(ValueError): self.C.divisao(10,0)
if __name__ == '__main__':
    unittest.main()
    
