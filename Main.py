#Main.py
#Universidad del Valle de Guatemala
#Alejandro Gómez 20347
#Gabriela Contreras 20213
#Creacion: 7-03-21
#Ultima Edicion: 7-03-21


#import simpy
from time import sleep
import sys
import statistics

def Bienvenida():
    Oraciones = "Bienvenido al simulador de programa de uso de colas"
    for char in Oraciones:
        sleep(0.005)
        sys.stdout.write(char)

def menu():
    print("\n","\033[4m","SIMULADOR",'\033[m',"\n")
    print (" 1. Iniciar simulación", "\n","2. Creditos", "\n", "3. Salir")

def Creditos():
    print("Creado por:")
    print("Alejandro Gomez")
    print("Paola Contreras")


Bienvenida()
print("\n")

#Menu

var = False
while var == False:
    menu()
    opcion = int(input("\n""\033[4m""Elija la opción que quiera:"'\033[m'""))
    if opcion == 1:
        print("Iniciando simulacion...")
        env = simpy.Environment() # Creation of the simulation
        env.run(until=10) # run simulation until the process number 10
    
        #for i in range():
            #TiempoTardaEnSimular =
            #MemoriaDisponible = Queue.Ram
            #InstruccionesBrindadas = Queue.nFunciones
            #env.process(algo tiene de argumento)
            #env.run()
    

    if opcion == 2:
        print("\n")
        Creditos()

    if opcion == 3:
        print("Saliendo el programa...")
        print("Gracias por utilizar nuestro programa jeje")
        var = True
env.process()# generate 