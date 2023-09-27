from Paciente import Paciente
from Ficha_atencion import Ficha_atencion
from NoHabitual import NoHabitual

class Habitual(Paciente):
    def __init__(self, nombre, rut, telefono, correo, tipo_paciente, info_prevision, ficha_atencion=[]):
        super().__init__(nombre, rut, telefono, correo, tipo_paciente)
        self._info_prevision = info_prevision
        self._ficha_atencion = ficha_atencion or []
    #Geterseter
    def get_info_prevision(self):
        return self._info_prevision
    def set_info_prevision(self, info_prevision):
        self._info_prevision = info_prevision
    def set_ficha_atencion(self, ficha):
        self.ficha_atencion.append(ficha)
    def get_ficha_atencion(self):
        return self.ficha_atencion
    
    #metodos
    def __str__(self):
        print("datos de habitual")
        print(super().__str__())
        return  f"\nInformación de previsión: {self.get_info_prevision() }"

    
    def crear_habitual(pacientes,medicos):
        nombre = input("Ingrese el nombre del paciente habitual: ")
        rut = input("Ingrese el RUT del paciente habitual: ")
        telefono = input("Ingrese el teléfono del paciente habitual: ")
        correo = input("Ingrese el correo del paciente habitual: ")
        info_prevision = input("Ingrese la información de previsión del paciente habitual: ")
        #agregar fichaaaaaaaaa
        #ficha_atencion=Habitual.agregar_ficha()
        ficha_atencion=""
        paciente= Habitual(nombre, rut, telefono, correo, "Habitual", info_prevision, ficha_atencion)
        paciente.agregar_ficha(medicos)
        pacientes.append(paciente)#el paciente esta en la pos -1 de la lista
        return pacientes #retorna una lista d elos pacientes
    
    def agregar_ficha(self, medicos):    #crear la ficha y agregar a registro(lista), se retorna registo
        
        ficha_atencion = Ficha_atencion.crear_ficha(medicos)
        self.set_ficha_atencion(self.get_ficha_atencion.append(ficha_atencion))
        #self._ficha_atencion.append(ficha_atencion)
        
        

    def cambio_tipo_paciente(self):
        nombre=self.get_nombre()
        rut=self.get_rut()
        correo=self.get_correo()
        telefono=self.get_telefono()
        diagnostico= NoHabitual.get_diagnostico(self)
        medico= NoHabitual.get_ultimo_medico()
        tipo="Habitual"
        info_prevision = input("Ingrese la información de previsión del paciente habitual: ")
        ficha_atencion = Ficha_atencion(medico,"None",diagnostico,"None")
        registro=[ficha_atencion]
        paciente= Habitual(nombre,rut,telefono,correo,tipo,info_prevision,registro)
        return paciente

        
    
    #Falta 
    #agregar la ficha en creal habitual
    #agregar ficha a registo