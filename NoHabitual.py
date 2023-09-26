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
    
    def __str__(self):
        return super().__str__() + f", Diagnóstico: {self.get_diagnostico()}, Último médico que lo atendió: {self.get_ultimo_medico()}"

    
    
    def crear_no_habitual(lista_medico):
        nombre = input("Ingrese el nombre del paciente: ")
        rut = input("Ingrese el RUT del paciente: ")
        while verificar(rut)==False:
            rut = input("Rut invalido, ingrese nuevamente: ")
        telefono = input("Ingrese el teléfono del paciente: ")
        correo = input("Ingrese el correo del paciente: ")
        diagnostico = input("Ingrese el diagnóstico del paciente: ")
        #escoje ultimo medico
        ultimo_medico=""
        print("----- Medicos ------")
        for index, a in enumerate(lista_medico):
            print(f"[{index}] {a}")
        if len(lista_medico)>1:
            op=int(input("Ingrese el nombre del último médico que lo atendió:"))
            while op>len(lista_medico) or op<0:
                op=int(input("----Valor invalido----\nIngrese una opcion: "))
            ultimo_medico= (lista_medico[op])
        else: 
            ultimo_medico,_ = Medico.Crear_medico()
            lista_medico.append(ultimo_medico)


        no_habitual = NoHabitual(nombre, rut, telefono, correo, NoHabitual,diagnostico, ultimo_medico)

        return no_habitual, lista_medico
        