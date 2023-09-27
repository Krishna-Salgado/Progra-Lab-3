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
        return super().__str__() +f"\nEspecialidad: {self.get_especialidad()}"
    
    def Crear_medico(lista_medicos):
        nombre = input("Ingrese el nombre del medico: ")
        try:
            rut = input("Ingrese el rut: ")
            while verificar(rut)==False:
                rut = input("Rut invalido, ingrese nuevamente: ")
        except ValueError:
            rut = input("Rut invalido, ingrese nuevamente: ")
            
        telefono = input("Ingrese el numero telefonico: ")
        correo = input("Ingrese el correo electronico: ")
        especialidad= input("Ingrese la especialidad: ")
        opera=Medico.es_cirujano(especialidad,listado_especialidad)
        #se crea la instancia de Medico
        medico=Medico(nombre, rut, telefono, correo, especialidad)
        lista_medicos.append(medico)
        return lista_medicos,opera

    def es_cirujano(especialidad,pueden_operar):
        for opera in pueden_operar:
            if especialidad.lower()==opera.lower():
                return True
        return False
    
    
    def verificar_medico(nombre, lista):
        for m in lista:
            if nombre.lower() == m.lower():
                print("medico encontrado")
                return True, lista
            else:
                print("Medico no encontrado, a continuacion cree el medico")
                medico = Medico.Crear_medico(lista)
                return False, lista
        
    def asignar_medico(lista_medico):
        for index, a in enumerate(lista_medico):
            print(f"[{index}] {a}")
        print(f"[{len(lista_medico)}] Agregar nuevo medico")
        if len(lista_medico)>=1:
            op=int(input("Ingrese el numero del último médico que lo atendió:"))
            while op>len(lista_medico) or op<0:
                op=int(input("----Valor invalido----\nIngrese una opcion: "))
            if op ==len(lista_medico):
                lista_medico,_ = Medico.Crear_medico(lista_medico)
                ultimo_medico=lista_medico[-1]
                lista_medico.append(ultimo_medico)
            else:
                ultimo_medico= (lista_medico[op])
        else: 
            print("No hay medicos disponible, ingresa los datos del nuevo medico")
            ultimo_medico,_ = Medico.Crear_medico(lista_medico)
            lista_medico.append(ultimo_medico)

        return ultimo_medico, lista_medico
