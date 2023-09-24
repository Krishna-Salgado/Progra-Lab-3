from Persona import Persona
class Paciente(Persona):
    def __init__(self, nombre, rut, telefono, correo, tipo_paciente):
        super().__init__(nombre, rut, telefono, correo)
        self._tipo_paciente = tipo_paciente
    
    def get_tipo_paciente(self):
        return self._tipo_paciente
    
    def set_tipo_paciente(self, tipo_paciente):
        self._tipo_paciente = tipo_paciente
    
    def __str___(self):
        return super().__str__() + f", Tipo de paciente: {self._tipo_paciente}"
    

    def verificar_paciente():
        pass
    def cambio_tipo_paciente():
        pass