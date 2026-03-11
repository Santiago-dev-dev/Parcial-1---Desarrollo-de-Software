# tests/test_funciones.py
import unittest
from src.funciones import hallar_maxima_nota  

class TestFunciones(unittest.TestCase):

    def test_hallar_maxima_nota(self):
        # Caso con notas válidas
        self.assertEqual(hallar_maxima_nota([3.5, 4.2, 5.0]), 5.0)
        
        # Caso con lista vacía
        self.assertEqual(hallar_maxima_nota([]), None)
        
        # Caso con notas entre 0 y 5
        self.assertEqual(hallar_maxima_nota([0, 1, 2, 4, 5]), 5)

if __name__ == "__main__":
    unittest.main()
