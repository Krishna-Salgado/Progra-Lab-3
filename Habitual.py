from Paciente import Paciente
from Ficha_antencion import Ficha_atencion

class Habitual(Paciente):
    def __init__(self, nombre, rut, telefono, correo, tipo_paciente, info_prevision, ficha_atencion=[]):
        super().__init__(nombre, rut, telefono, correo, tipo_paciente)
        self._info_prevision = info_prevision
        self._ficha_atencion = ficha_atencion
    
    def agregar_ficha_atencion(self, ficha):
        self.ficha_atencion.append(ficha)

    def mostrar_ficha_atencion(self):
        return self.ficha_atencion

    def __str__(self):
        return f"{super().__str__()}\nInformación de previsión: {self.info_prevision}"

    
    def crear_habitual(cls):
        nombre = input("Ingrese el nombre del paciente habitual: ")
        rut = input("Ingrese el RUT del paciente habitual: ")
        telefono = input("Ingrese el teléfono del paciente habitual: ")
        correo = input("Ingrese el correo del paciente habitual: ")
        info_prevision = input("Ingrese la información de previsión del paciente habitual: ")
        ficha_atencion = Ficha_atencion.crear_ficha()
        return cls(nombre, rut, telefono, correo, "Habitual", info_prevision, ficha_atencion)