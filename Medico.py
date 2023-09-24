from Persona import Persona
from Verificar_Rut import Verificar_rut as verificar
from Archivo_configuraciones import listado_especialidad
class Medico(Persona):
    def __init__(self,nombre, rut, telefono, correo, especialidad):
        super().__init__(nombre, rut, telefono, correo)
        self.especialidad = especialidad

    def get_especialidad(self):
        return self.__especialidad
    def set_especialidad(self,especialidad):
        self.__especialidad = especialidad
    
    #Metodos
    def __str__(self):
        return f"Especialidad: {self.get_especialidad()}"
    
    def Crear_medico():
        nombre = input("Ingrese el nombre del medico: ")
        rut = input("Ingrese el rut: ")
        while verificar(rut)==False:
            rut = input("Rut invalido, ingrese nuevamente: ")
        
        telefono = input("Ingrese el numero telefonico: ")
        correo = input("Ingrese el correo electronico: ")
        especialidad= input("Ingrese la especial: ")
        opera=Medico.Verificar_medico(especialidad,listado_especialidad)
        
        medico=Medico(nombre, rut, telefono, correo, especialidad)
        return medico,opera

    def Verificar_medico(especialidad,pueden_operar):
        for opera in pueden_operar:
            if especialidad==opera:
                return True
        return False
