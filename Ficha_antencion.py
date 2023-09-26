from Medico import Medico 
from Main import lista_medicos

class Ficha_atencion():
    def __init__(self, medico,fecha_atencion,diagnostico,valor):
        self.__medico = medico
        self.__fecha_atencion = fecha_atencion
        self.__diagnostico = diagnostico
        self.__valor = valor

    def get_medico(self):
        return self.__medico
    def get_fecha_atencion(self):
        return self.__fecha_atencion
    def get_diagnostico(self):
        return self.__diagnostico
    def get_valor(self):
        return self.__valor
    
    def set_(self,medico):
        self.__medico = medico
    def set_fecha_atencion(self,fecha_atencion):
        self.__fecha_atencion = fecha_atencion
    def set_diagnostico(self,diagnostico):
        self.__diagnostico= diagnostico
    def set_valor(self,valor):
        self.__valor = valor



    def crear_ficha():
        nombre = ("Ingrese el medico a cargo: ")
        while Ficha_atencion.verificar_nombre_medico(nombre, lista_medicos)==False:
            nombre = ("Medico no existente, ingrese el medico a cargo: ")
        fecha_atencion = ("Ingrese la fecha de atencion: ")
        diagnostico = ("Ingrese el diagnostico: ")
        valor = ("Ingrese el valor de la atencion: ")
        ficha = Ficha_atencion(nombre, fecha_atencion, diagnostico, valor)
        return ficha


    def verificar_nombre_medico(nombre, lista):
        if nombre in lista:
            return True
        else:
            return False

    def __str__(self):
        return f"Medico a cargo: \n{Medico.__str__(self.get_medico())} \nDiagnostico: {self.get_diagnostico()}, Fecha de atencion: {self.get_fecha_atencion()}\nValor: {self.get_valor()}"




