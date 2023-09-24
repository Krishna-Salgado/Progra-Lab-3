from Paciente import Paciente
class NoHabitual(Paciente):
    def __init__(self, nombre, rut, telefono, correo, tipo_paciente, diagnostico, ultimo_medico):
        super().__init__(nombre, rut, telefono, correo, tipo_paciente)
        self._diagnostico = diagnostico
        self._ultimo_medico = ultimo_medico
    
    def get_diagnostico(self):
        return self._diagnostico
    def get_ultimo_medico(self):
        return self._ultimo_medico
    
    def set_diagnostico(self, diagnostico):
        self._diagnostico = diagnostico
    def set_ultimo_medico(self, ultimo_medico):
        self._ultimo_medico = ultimo_medico
    
    def __str__(self):
        return super().__str__() + f", Diagnostico: {self._diagnostico}, Ultimo medico que lo atendio: {self._ultimo_medico} "
    
    def crear():
        pass