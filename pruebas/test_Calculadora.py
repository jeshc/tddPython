import sys
sys.path.insert(0, "./src")
import unittest
from Matematicas import Calculadora



class probarCalculadora(unittest.TestCase):
    def test_constructor_ver_uno(self):
        calculadora = Calculadora(0,0,0)
        self.assertEqual(0,calculadora.getOperandoUno())

    def test_constructor_ver_dos(self):
        calculadora = Calculadora(0,0,0)
        self.assertEqual(0,calculadora.getOperandoDos())

    def test_constructor_ver_tres(self):
        calculadora = Calculadora(0,0,0)
        self.assertEqual(0,calculadora.getOperador())

    def test_Suma(self):
        calculadora = Calculadora(2,3,1)
        self.assertEqual(5,calculadora.sumar())
