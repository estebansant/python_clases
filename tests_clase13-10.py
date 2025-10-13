import unittest
from clase13_10 import suma_total

class Test_suma_total(unittest.TestCase):
    def test_1(self):
        s=[1,2,3,4]
        res_obtenido = suma_total(s)
        res_esperado = 10
        self.assertEqual(res_obtenido,res_esperado)

if __name__ == "__main__":
    unittest.main(verbosity=2)
