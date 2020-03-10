class Calculadora:
    def __init__(self):
        self.__operandoUno=0
        self.__operandoDos=0
        self.__operador=0

    def getOperandoUno(self):
        return self.__operandoUno

    def getOperandoDos(self):
        return self.__operandoDos

    def getOperador(self):
        return self.__operador

calc=Calculadora()
print(calc.getOperandoUno())
