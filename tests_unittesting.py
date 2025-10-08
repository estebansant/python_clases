import unittest
from unittesting import es_multiplo_de, devolver_el_doble_si_es_par, fahrenheit_a_celsius

class test_es_multiplo_de(unittest.TestCase):
    def test_multiplo_par(self):
        self.assertTrue(es_multiplo_de(4,2))
    def test_multiplo_impar(self):
        self.assertTrue(es_multiplo_de(9,3))
    def test_no_multiplo_par(self):
        self.assertFalse(es_multiplo_de(7,2))
    def test_no_multiplo_impar(self):
        self.assertFalse(es_multiplo_de(14,3))
    def test_no_multiplo_mayor(self):
        self.assertFalse(es_multiplo_de(3,9))


class test_devolver_el_doble_si_es_par(unittest.TestCase):
    def test_devolver_doble_par(self):
        self.assertEqual(devolver_el_doble_si_es_par(10), 20)
    def test_devolver_impar(self):
        self.assertEqual(devolver_el_doble_si_es_par(3),3)

class test_fahrenheit_a_celsius(unittest.TestCase):
    def test_fahrenheit_100(self):
        self.assertAlmostEqual(fahrenheit_a_celsius(100),37.77,delta=0.01)
    def test_fahrenheit_451(self):
        self.assertAlmostEqual(fahrenheit_a_celsius(451),232.778,delta=0.01)



if __name__ == '__main__':
    unittest.main(verbosity=2)
