from Persona import Persona
from Medico import Medico
from Cirujano import Cirujano
from Archivo_configuraciones import *
from NoHabitual import NoHabitual


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
#medico,opera=Medico.Crear_medico()
#if opera==True:
#    medico=Cirujano.Crear_Cirujano(medico)
#lista_medicos.append(medico)

nh= NoHabitual.crear_no_habitual(lista_medicos)
#NoHabitual.__str__(nh)
resultado_str = NoHabitual.__str__(nh)
print(resultado_str)