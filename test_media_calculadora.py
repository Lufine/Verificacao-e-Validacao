import unittest
from media_calculadora import calcular_media  # Importa a função a ser testada

class TestCalcularMedia(unittest.TestCase):
    
    def test_media_basica(self):
        self.assertEqual(calcular_media(7, 8, 9), 8)
    
    def test_todas_notas_zero(self):
        self.assertEqual(calcular_media(0, 0, 0), 0)
        
    def test_todas_notas_maximas(self):
        self.assertEqual(calcular_media(10, 10, 10), 10)
        
    def test_notas_decimais(self):
        self.assertAlmostEqual(calcular_media(8.5, 7.3, 6.8), 7.53, places=2)

if __name__ == "__main__":
    unittest.main()
