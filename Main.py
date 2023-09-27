from Persona import Persona
from Medico import Medico
from Cirujano import Cirujano
from Archivo_configuraciones import *
from NoHabitual import NoHabitual
from Habitual import Habitual
lista_medicos=[]
lista_pacientes=[]

def main_menu(lista_medicos,lista_pacientes):   
    opcion = 1

    while int(opcion > 0) and int(opcion <= 5):
        print("\n--- Menú ---")
        print("1. Crear Médico ")
        print("2. Crear Paciente")
        print("3. Mostrar Médicos")
        print("4. Mostrar Pacientes")
        print("5. Mostrar Registro de Atención")
        print("0. Salir")

        bandera = 1
        while bandera == 1:
            try:
                opcion = int(input("Ingrese una opción: "))
                if int(opcion >=0) and int(opcion<=5):   
                    bandera = 0   
                else:
                    print("Opción elegida equivocada ")
            except ValueError:
                print("Ingrese una opción nuevamente entre 0 y 5")

        if opcion == 1:
            lista_medicos,opera=Medico.Crear_medico(lista_medicos)
            medico=lista_medicos[-1]
            if opera==True:
                medico=Cirujano.Crear_Cirujano(medico)
                lista_medicos.pop()
                lista_medicos.append(medico)
                medico.__str__()
            else: print(medico)


        elif opcion == 2:
            lista_medicos,lista_pacientes, existe =NoHabitual.crear_no_habitual(lista_medicos, lista_pacientes)
            if existe== True:
                paciente=Habitual.cambio_tipo_paciente(lista_pacientes[-1])
                lista_pacientes.pop()
                lista_pacientes.append(paciente)

        elif opcion == 3:
            for i in lista_medicos:
                print("op3")
                if type(i)== Cirujano:
                    i.__str__()
                else:
                    print(i) 

        elif opcion == 4:
            for i in lista_pacientes:
                print(i)   

        elif opcion == 5:
            pass
        elif opcion == 0:
            print("¡Hasta luego!")

main_menu(lista_medicos,lista_pacientes)
"""
print("wena")
#opcion crear medico
medicos,opera=Medico.Crear_medico(lista_medicos)
medico=medicos[-1]
if opera==True:
    medico=Cirujano.Crear_Cirujano(medico)

print("aaaaaa")
for i in lista_medicos:
    print(i)
"""
#lista_medico,pacientes= NoHabitual.crear_no_habitual(lista_medicos,lista_pacientes)
#paciente=pacientes[-1]
#NoHabitual.__str__(paciente)
#h= Habitual.crear_habitual(lista_pacientes, lista_medicos)
#Habitual.__str__(h[-1])

#print("pueba verificar")
#medico= Medico("pepito","123","890","gamil","cardiologo")
#lista_medicos.append(medico)
#Medico.verificar_nombre_medico("juan",lista_medicos)
#print("buscando al pepito")
#Medico.verificar_nombre_medico("pepito",lista_medicos)
#
#for i in lista_medicos:
#    i.__str__()
#print("seacabo")