class Calculadora:

    def __init__(self, op1,op2,operador):
        self.__operandoUno=op1
        self.__operandoDos=op2
        self.__operador=operador

    def getOperandoUno(self):
        return self.__operandoUno

    def getOperandoDos(self):
        return self.__operandoDos

    def getOperador(self):
        return self.__operador

    def sumar( self ):
        return self.__operandoUno + self.__operandoDos
        
