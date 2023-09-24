from Medico import Medico 

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

    def __str__(self):
        return f"Medico a cargo: \n{Medico.__str__(self.get_medico())} \nDiagnostico: {self.get_diagnostico()}, Fecha de atencion: {self.get_fecha_atencion()}\nValor: {self.get_valor()}"




