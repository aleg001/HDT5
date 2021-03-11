#Event.py
#Universidad del Valle de Guatemala
#Alejandro Gómez 20347
#Gabriela Contreras 20213
#Creacion: 7-03-21
#Ultima Edicion: 11-03-21

#Imports
import simpy
import random as r

#Variables
#RAM_Max = 25
#Instrucc = 3

class SYS:
    #Constructor of SYS 
    def __init__(self, env):
        self.RandomAccess = simpy.Container(env, init= RAM_Max, capacity= RAM_Max)
        self.CentralProccess = simpy.Resource(env, capacity=1)

class Event:
    #Atributtes 
    waiting_list=list()

    #Constructor
    def __init__(self, environment: simpy.Environment, cpu: simpy.Resource, wait: simpy.Resource, ram: simpy.Container):
        
        self.__ENVIRONMENT = environment
        
        self.__CentralProcessingUnit = cpu
        
        self.__Esperar = wait
        
        self.__RandomAccessMemory = ram
        #Tiempo
        self.__Time = []
        #Tiempo Total
        self.__TotalTime = 0
        
        self.__TimeL = 0
    
    #Functions that works like Getters 
    def getTime(self):
        return self.__Time

    def getTotalTime(self):
        return self.__TotalTime

    #
    def ProcesamientoDeInstructions(self, nombre: str, ram: int, instrucciones: int, speed: int):
            
            #Method to give and amount of RAM to a process 
            yield self.__ENVIRONMENT.timeout(len(self.__Time))
            print(f"{nombre}")
            print("Usted necesita {ram} para su ejecución.")
            self.__TimeL = self.__ENVIRONMENT.now

            yield self.__RandomAccessMemory.get(ram)

            print(f"Felicidades {nombre}, su solicitud ha sido aceptada")
            print("La cantidad de RAM: {ram}.")

            iTerminadas = 0 #counter 
            #cycle thata allows the CPU to execute a process 
            while iTerminadas < instrucciones:

                with self.__CentralProcessingUnit.request() as request:
                    yield request

                    if (instrucciones - iTerminadas) >= speed:
                        nInstrucciones = speed
                    else:
                        nInstrucciones = (instrucciones - iTerminadas)

                    print(f"El CPU se encuenta ejecutando {nInstrucciones} instrucciones.")
                    yield self.__ENVIRONMENT.timeout(nInstrucciones/speed)

                    iTerminadas += nInstrucciones
                    print(f"{iTerminadas} / {instrucciones} finalizadas.")
                    print("\n")

                decision = r.randint(1, 2)

                if iTerminadas < instrucciones and decision == 1:

                    with self.__Esperar.request() as new_request:
                        yield new_request
                        yield self.__ENVIRONMENT.timeout(1)
                        print("Realizando proceso...")
                        print("FELICIDADES!!!")
                        print("Las operaciones de entrada y salida han sido terminadas.")

            yield self.__RandomAccessMemory.put(ram)
            print("\n")
            print(f"RAM utilizada: {ram}")
            self.__TotalTime += (self.__ENVIRONMENT.now - self.__TimeL)
            self.__Time.append(self.__ENVIRONMENT.now - self.__TimeL)


    # function that shows the information to the user
    def show(self):
        print ("Proceso:",self.eventname, "memoria: ", self.eventmemory, "instrucciones necesarias: ",self.eventinstructions)

    # functions that return us data useful for the program  
    def name(self):
        return self.eventname

    def memory(self):
        return self.eventmemory

    def instructions(self):
        return self.eventinstructions

    def terminar(self):
        return self.eventinstructions<= 0
        numer = 0

    #Inatructions for the process 
    def procesosCorrespondientes(self, env, syso):
        inicia = env.now
        self.cT = inicia
        print("%s El tiempo estimado fue de  %d" %(env, syso))
        
        with syso.RAM.get(self.memory) as gRam:
            yield gRam

        print("Procesando...")
        print("%s: Tiene esta RAM:  %d Estado: Waiting" %(self.eventname, env.now))
        while not self.terminarProceso:
            with syso.CPU.request() as ricues:
                print("%s: Su CPU se encuentra en %d Estado: Waiting" %(self.eventname, env.now))
                yield ricues
                print("%s: Su CPU se encuentra en %d Estado: Running" %(self.eventname, env.now))
                for i in range(Instrucc):
                    if self.instructions > 0:
                        self.instuctions -= 1
                        nextOperation = r.randint(1,2)
                yield env.timeout(nextOperation)


