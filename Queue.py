#Queue.py
#Universidad del Valle de Guatemala
#Alejandro Gómez 20347
#Gabriela Contreras 20213
#Creacion: 7-03-21
#Ultima Edicion: 7-03-21

#Imports
import random as r
#import simpy as s

#Se crean instancias

#env = s.Environment()
#RandomAccessMemory = s.Container(env, init = 1, capacity = 10)
#CentralPorcessingUnit = s.Resource(env, capacity = 1)
numer = 0

#Se definen funciones a utilizar
def RAM():
    numero = r.randint(1,10)
    print("La cantidad de memoria disponible es: ",numero) 

def nFunciones():
    func = r.randint(1,10)
    print("Las instrucciones generadas son: ", func)

def genProceso(env, variableNueva):
    while True: 
        print("Procesando...")
        yield env.timeout(variableNueva)

def AvailableSpace(numer):
    if(numer < 0):
        print("Ups!! Se ha quedado sin espacio")
        print("Su proceso, pasará a la cola jeje... :O")
    elif(numer <=10):
        print("Iniciando proceso...")
        print("Sea paciente porfavo!!")


numer = RAM()
    

