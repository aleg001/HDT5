#Main.py
#Universidad del Valle de Guatemala
#Alejandro Gómez 20347
#Gabriela Contreras 20213
#Creacion: 7-03-21
#Ultima Edicion: 11-03-21

import sys
import simpy 
import statistics
import Menu as mn
import Event as e
import random as r 
from time import sleep 

#Variables
opcion=0
var = False
mn.menu()
Speed = 3
Ram = 10
Pro = 25
opcion = 0
Env = simpy.Environment()

Procesamiento = e.Event(
    Env,
    simpy.Resource(Env, capacity = 1),
    simpy.Resource(Env, capacity = 2),
    simpy.Container(Env, init = Ram, capacity = Ram)
)

Intervals = 25
r.seed(777)

def comprob(opcion):
    """Se define función para comprobar el valor ingresado."""
    
    num = False
    while num == False:
        try:
            """ El valor ingresado se convierte en int y se valida """
            
            opcion = int(opcion)
            num = True
        except ValueError:
            """ En caso el valor no sea válido, se pide nuevamente el ingreso """
            
            print("Error, solo puede ingresar números")
            opcion = input("Intente nuevamente: ")
    return opcion

#Main function is defined
def main():
    
    Env.run()
    #Everything related to math procesess is made
    averageTime = (Procesamiento.getTotalTime() / Pro)
    print(f"\nTiempo promedio: {averageTime}")
    StandarDeviation = statistics.stdev(Procesamiento.getTime())
    print(f"\nDesviación estándar: {StandarDeviation}")
#For cycle to go through the proccess
for i in range(Pro):
    tiempo = r.expovariate(1 / Intervals)
    nInstrucciones = r.randint(1, 10)
    randomRam = r.randint(1, 10)
    Env.process(Procesamiento.ProcesamientoDeInstructions(
        f"Proceso número: {i}",
        randomRam,
        nInstrucciones,
        Speed
    ))



while var == False:
    #Defensive program for an input
    try:
        print("\n")
        opcion=(input("\033[4m""Elija la opción que quiera:""\033[0m"" "))
        print("\n")
        opcion = comprob(opcion)

    except ValueError:
        mn.Error()

# Available Operations  
    if opcion == 1:
        #Cicle of the program 
        mn.Iniciar()
        mn.Bienvenida()
        main()
        mn.menu()

    if opcion == 2:
        #Authors of the credits
        mn.Creditos()
        mn.menu()

    if opcion == 3:
        print("\n")
        mn.Salida()
        var = True #breaks cicle 