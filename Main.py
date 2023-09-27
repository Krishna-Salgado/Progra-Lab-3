from Persona import Persona
from Medico import Medico
from Cirujano import Cirujano
from Archivo_configuraciones import *
from NoHabitual import NoHabitual
from Habitual import Habitual
lista_medicos=[]
lista_pacientes=[]

def Menu():
    print("\n------ Menu ------")
    print("1.- ")
    op=int(input("Ingrese una opcion: "))
    while op < 9 and op>0:
        op=int(input("Ingrese una opcion: "))
    if op ==1:
        pass

print("wena")
#opcion crear medico
#medicos,opera=Medico.Crear_medico()
#medico=medicos[-1]
#if opera==True:
#    medico=Cirujano.Crear_Cirujano(medico)
#lista_medicos.append(medico)

#lista_medico,pacientes= NoHabitual.crear_no_habitual(lista_medicos,lista_pacientes)
#paciente=pacientes[-1]
#NoHabitual.__str__(paciente)
#h= Habitual.crear_habitual(lista_pacientes, lista_medicos)
#Habitual.__str__(h[-1])

print("pueba verificar")
medico= Medico("pepito","123","890","gamil","cardiologo")
lista_medicos.append(medico)
Medico.verificar_nombre_medico("juan",lista_medicos)
print("buscando al pepito")
Medico.verificar_nombre_medico("pepito",lista_medicos)

for i in lista_medicos:
    i.__str__()
print("seacabo")