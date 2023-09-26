from Medico import Medico
from Verificar_Rut import Verificar_rut as verificar
from Archivo_configuraciones import *

class Cirujano(Medico):
    def __init__(self,nombre, rut, telefono, correo, especialidad,operaciones, anestesistas, enfermeras):
        super().__init__(nombre, rut, telefono, correo,especialidad)
        self.__operaciones = operaciones
        self.__anestesistas = anestesistas
        self.__enfermeras = enfermeras

    def get_operaciones(self):
        return self.__operaciones
    def get_anestesistas(self):
        return self.__anestesistas
    def get_enfermeras(self):
        return self.__enfermeras
    
    def set_operaciones(self,operaciones):
        self.__operaciones = operaciones
    
    def set_anestesistas(self,anestesistas):
        self.__anestesistas = anestesistas
    
    def set_enfermeras(self,enfermeras):
        self.__enfermeras = enfermeras
    
    #Metodos
    def __str__(self):
        p,pp=Medico.__str__(self)
        print( p ,pp, f"- Operaciones realizadas: {self.get_operaciones()}\nEnfermeras: {self.get_enfermeras()}\nAnestesistas: {self.get_anestesistas()}")
    
    def Crear_Cirujano(medico):
        operaciones= input("Ingrese cantidad de operaciones realizadas: ")
        anestesistas=[]
        enfermeras= []
        #agrgar anestesistas
        flag = True
        while flag:
            print("----- Anestesistas -----")
            for index, a in enumerate(lista_anestesistas):
                print(f"[{index}] {a}")
            op=int(input("Ingrese una opcion: "))
            while op>len(lista_anestesistas) or op<0:
                op=int(input("----Valor invalido----\nIngrese una opcion: "))
            anestesistas.append(lista_anestesistas[op])
            op=int(input("Quiere asignar otro anestesista a este medico? [1] Si [2] No"))
            if op ==2:
                flag = False
        #agregar enfermeras
        flag = True
        while flag:
            print("----- Enfermeras ------")
            for index, a in enumerate(lista_enfermeras):
                print(f"[{index}] {a}")
            op=int(input("Ingrese una opcion: "))
            while op>len(lista_enfermeras) or op<0:
                op=int(input("----Valor invalido----\nIngrese una opcion: "))
            enfermeras.append(lista_enfermeras[op])
            op=int(input("Quiere asignar otra enfermera a este medico? [1] Si [2] No"))
            if op ==2:
                flag = False
        nombre=medico.get_nombre()
        rut= medico.get_rut() 
        telefono= medico.get_telefono()
        correo=medico.get_correo()
        especialidad=medico.get_especialidad()

        cirujano= Cirujano(nombre,rut, telefono, correo,especialidad,operaciones,anestesistas,enfermeras)
        cirujano.__str__()
        return cirujano