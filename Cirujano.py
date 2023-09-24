from Medico import Medico
class Cirujano(Medico):
    def __init__(self,nombre, rut, telefono, correo, especialidad,operaciones, anestesistas, enfermeras):
        super().__init__(nombre, rut, telefono, correo,especialidad)
        self._operaciones = operaciones
        self._anestesistas = anestesistas
        self._enfermeras = enfermeras

    def get_operaciones(self):
        return self.__operaciones
    def get_anestesistas(self):
        return self.__anestesistas
    def get_enfermeras(self):
        return self.__enfermeras
    
    def set_operaciones(self,operaciones):
        self.__operaciones = operaciones
    
    def set_anestesistas(self,anestesistas):
        self.__anestesistas = anestesistas
    
    def set_enfermeras(self,enfermeras):
        self.__enfermeras = enfermeras
    
    #Metodos
    def __str__(self):
        return super.__str__(self) , f"Operaciones realizadas: {self.get_operaciones()}\nEnfermeras: {self.get_enfermeras()}\nAnestesistas: {self.get_anestesistas()}"
    
    def Crear_Cirujano():
        pass