from Persona import Persona
class Paciente(Persona):
    def __init__(self, nombre, rut, telefono, correo, tipo_paciente="Habitual"):
        super().__init__(nombre, rut, telefono, correo)
        self._tipo_paciente = tipo_paciente
    
    def get_tipo_paciente(self):
        return self._tipo_paciente
    def set_tipo_paciente(self, tipo_paciente):
        self._tipo_paciente = tipo_paciente
    
    #metodos
    def __str__(self):
        return super().__str__() + f", Tipo de paciente: {self._tipo_paciente}"    

    def verificar_tipo_paciente(self):
        if self.tipo_paciente.lower() == "No Habitual".lower():
            #Se puede realizar cambio de Clase
            return True
