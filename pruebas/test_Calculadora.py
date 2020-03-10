import sys
sys.path.insert(0, "./src")
import unittest
from Matematicas import Calculadora



class probarCalculadora(unittest.TestCase):
    def test_constructor_defecto(self):
        calculadora = Calculadora()
        self.assertEqual(0,calculadora.getOperandoUno())
