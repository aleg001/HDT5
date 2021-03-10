#Event.py
#Universidad del Valle de Guatemala
#Alejandro Gómez 20347
#Gabriela Contreras 20213
#Creacion: 7-03-21
#Ultima Edicion: 7-03-21

#Imports
import simpy
import random as r

RAM_Max = 100
Instrucc = 6

class SYS:
    def __init__(self, env):
        self.RandomAccess = simpy.Container(env, init= RAM_Max, capacity= RAM_Max)
        self.CentralProccess = simpy.Resource(env, capacity=1)

class Event:
    #Atributtes 
    waiting_list=list()

    #Constructor
    def __init__(self, name, memory, instructions, env, syso):
        self.eventname = name
        self.eventmemory = memory
        self.eventinstructions = instructions
        self.Process = env.process(self.procesosCorrespondientes(env, syso))
        self.cT = 0
        self.fT = 0
        self.TiempoTotal = 0
        self.env = env
        self.SYS = syso
        self.terminarProceso = False

    def show(self):
        print ("Proceso:",self.eventname, "memoria: ", self.eventmemory, "instrucciones necesarias: ",self.eventinstructions)

    def name(self):
        return self.eventname

    def memory(self):
        return self.eventmemory

    def instructions(self):
        return self.eventinstructions

    def terminar(self):
        return self.eventinstructions<= 0
        numer = 0



    def procesosCorrespondientes(self, env, syso):
        in1 = env.now
        self.cT = in1
        print("%s Se ha tardado %d" %(env, syso))
        
        with syso.RAM.get(self.memory) as gRam:
            yield gRam
        
        print("Procesando...")
        print("%s: Ha obtenido RAM en %d Estado: Waiting" %(self.eventname, env.now))
        while not self.terminarProceso:
            with syso.CPU.request() as ricues:
                print("%s: CPU en %d Estado: Waiting" %(self.eventname, env.now))
                yield ricues
                print("%s: CPU en %d Estado: Running" %(self.eventname, env.now))
                for i in range(Instrucc):
                    if self.instructions > 0:
                        self.instuctions -= 1
                        nextOperation = r.randint(1,2)
                yield env.timeout(nextOperation)


    



    #def Procesos():
        #for i in range(10):
           # raM = r.randint(1,10)
         #   proc = r.randint(1,10)

