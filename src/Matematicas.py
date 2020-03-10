class Calculadora:
    def __init__(self):
        self.__operadorUno=0
        self.__operadorDos=0
        self.__operando=0

    def getOperandoUno(self):
        return self.__operadorUno

calc=Calculadora()
print(calc.getOperandoUno())
