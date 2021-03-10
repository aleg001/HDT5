import random as r

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
#---------------------------------------------------------------------------------------------