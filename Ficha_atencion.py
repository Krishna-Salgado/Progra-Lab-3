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

    def crear_ficha(lista_medicos):
        nombre = input("Ingrese el medico a cargo: ")
        bool, lista_medicos= Medico.verificar_medico(nombre, lista_medicos)
        while bool==False:
            nombre = input("Ingrese el medico a cargo: ")

        fecha_atencion = input("Ingrese la fecha de atencion: ")
        diagnostico = input("Ingrese el diagnostico: ")
        valor = input("Ingrese el valor de la atencion: ")
        ficha = Ficha_atencion(nombre, fecha_atencion, diagnostico, valor)
        mostrar = Ficha_atencion.__str__(Ficha_atencion)
        return ficha, mostrar


    def __str__(self):
        print("-Ficha de atencion-")
        print("Medico a cargo:", Medico.__str__(self.get_medico()))
        return f"\nDiagnostico: {self.get_diagnostico()}, Fecha de atencion: {self.get_fecha_atencion()}\nValor: {self.get_valor()}"


#Falta crear. str

