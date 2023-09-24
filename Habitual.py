from Paciente import Paciente
class Habitual(Paciente):
    def __init__(self, nombre, rut, telefono, correo, tipo_paciente, info_prevision, ficha_atencion):
        super().__init__(nombre, rut, telefono, correo, tipo_paciente)
        self._info_prevision = info_prevision
        self._ficha_atencion = ficha_atencion
    
    def get_info_prevision(self):
        return self._info_prevision
    

    def set_info_prevision(self, info_prevision):
        self._info_prevision = info_prevision

    def __str__(self):
        return super().__str__() + f", Informacion de su prevision: {self._info_prevision}, "