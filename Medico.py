from Persona import Persona
from Verificar_Rut import Verificar_rut as verificar
from Archivo_configuraciones import listado_especialidad
class Medico(Persona):
    def __init__(self,nombre, rut, telefono, correo, especialidad):
        super().__init__(nombre, rut, telefono, correo)
        self.__especialidad = especialidad

    def get_especialidad(self):
        return self.__especialidad
    def set_especialidad(self,especialidad):
        self.__especialidad = especialidad
    
    #Metodos
    def __str__(self):
        print("----- Datos del medico ------")
        return Persona.__str__(self),f"\nEspecialidad: {self.get_especialidad()}"
    
    def Crear_medico():
        nombre = input("Ingrese el nombre del medico: ")
        rut = input("Ingrese el rut: ")
        while verificar(rut)==False:
            rut = input("Rut invalido, ingrese nuevamente: ")
        
        telefono = input("Ingrese el numero telefonico: ")
        correo = input("Ingrese el correo electronico: ")
        especialidad= input("Ingrese la especialidad: ")
        opera=Medico.es_cirujano(especialidad,listado_especialidad)
        #se crea la instancia de Medico
        medico=Medico(nombre, rut, telefono, correo, especialidad)
        return medico,opera

    def es_cirujano(especialidad,pueden_operar):
        for opera in pueden_operar:
            if especialidad.lower()==opera.lower():
                return True
        return False
