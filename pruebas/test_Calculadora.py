import sys
sys.path.insert(0, "./src")
import unittest
from Matematicas import Calculadora



class probarCalculadora(unittest.TestCase):
    def test_constructor_ver_uno(self):
        calculadora = Calculadora()
        self.assertEqual(0,calculadora.getOperandoUno())

    def test_constructor_ver_dos(self):
        calculadora = Calculadora()
        self.assertEqual(0,calculadora.getOperandoDos())

    def test_constructor_ver_tres(self):
        calculadora = Calculadora()
        self.assertEqual(0,calculadora.getOperador())
