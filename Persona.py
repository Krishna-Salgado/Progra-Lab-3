class Persona:
    def __init__(self, nombre, rut, telefono, correo):
        self._nombre = nombre
        self._rut = rut
        self._telefono = telefono
        self._correo = correo

    def get_nombre(self):
        return self._nombre
    def get_rut(self):
        return self._rut
    def get_telefono(self):
        return self._telefono
    def get_correo(self):
        return self._correo
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    def set_rut(self, rut):
        self._rut = rut
    def set_telefono(self, telefono):
        self._telefono = telefono
    def set_correo(self, correo):
        self._correo = correo
    
    
    def __str__(self):
        return f"Nombre: {self._nombre}, RUT: {self._rut}, Teléfono: {self._telefono}, Correo electronico: {self._correo}"