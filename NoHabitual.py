from Paciente import Paciente
from Verificar_Rut import Verificar_rut as verificar
from Medico import Medico

class NoHabitual(Paciente):
    def __init__(self, nombre, rut, telefono, correo, tipo_paciente, diagnostico, ultimo_medico):
        super().__init__(nombre, rut, telefono, correo, tipo_paciente)
        self.__diagnostico = diagnostico
        self._ultimo_medico = ultimo_medico
    
    def get_diagnostico(self):
        return self.__diagnostico
    def get_ultimo_medico(self):
        return self._ultimo_medico
    
    def set_diagnostico(self, diagnostico):
        self._diagnostico = diagnostico
    def set_ultimo_medico(self, ultimo_medico):
        self._ultimo_medico = ultimo_medico
    
    def mostrar_nohabitual(self):
        print("\n-----Informacion del paciente -----")
        print(super().__str__())
        print(f"Diagnóstico: {self.get_diagnostico()}")
        print(Medico.__str__(self.get_ultimo_medico()))
    
    def crear_no_habitual(lista_medico,pacientes):
        nombre = input("Ingrese el nombre del paciente: ")
        try:
            rut = input("Ingrese el RUT del paciente: ")
            while verificar(rut)==False:
                rut = input("Rut invalido, ingrese nuevamente: ")
        except ValueError:
            rut = input("Rut invalido, ingrese nuevamente: ")
        telefono = input("Ingrese el teléfono del paciente: ")
        correo = input("Ingrese el correo del paciente: ")
        diagnostico = input("Ingrese el diagnóstico del paciente: ")
        #escoje ultimo medico
        ultimo_medico, lista_medico = Medico.asignar_medico(lista_medico)
        no_habitual = NoHabitual(nombre, rut, telefono, correo, "No Habitual",diagnostico, ultimo_medico)

        existe= Paciente.verificar_existencia(pacientes,rut)
        pacientes.append(no_habitual)

        NoHabitual.mostrar_nohabitual(no_habitual)
        
        return lista_medico,pacientes, existe