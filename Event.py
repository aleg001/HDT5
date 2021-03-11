#Event.py
#Universidad del Valle de Guatemala
#Alejandro Gómez 20347
#Gabriela Contreras 20213
#Creacion: 7-03-21
#Ultima Edicion: 11-03-21

#Imports
import simpy
import random as r

#Event class is declared:

class Event:
    #Atributtes 
    waiting_list=list()

    #Constructor
    def __init__(self, environment: simpy.Environment, cpu: simpy.Resource, wait: simpy.Resource, ram: simpy.Container):
        
        #Environment is defined
        self.__ENVIRONMENT = environment
        #CPU used
        self.__CentralProcessingUnit = cpu
        #Wait
        self.__Esperar = wait
        #RAM used
        self.__RandomAccessMemory = ram
        #Time
        self.__Time = []
        #Total time
        self.__TotalTime = 0
        #Time in operations
        self.__TimeL = 0
    
    #Functions that works like Getters 
    def getTime(self):
        return self.__Time

    def getTotalTime(self):
        return self.__TotalTime

    #All of the processes needed for the simulation
    def ProcesamientoDeInstructions(self, nombre: str, ram: int, instrucciones: int, speed: int):
            
            #Method to give and amount of RAM to a process 
            yield self.__ENVIRONMENT.timeout(len(self.__Time))
            print(f"{nombre}")
            print("Usted necesita {ram} para su ejecución.")
            self.__TimeL = self.__ENVIRONMENT.now

            yield self.__RandomAccessMemory.get(ram)
            #Prints for each request made
            print(f"Felicidades {nombre}, su solicitud ha sido aceptada")
            print("La cantidad de RAM: {ram}.")

            iTerminadas = 0 #counter 
            #cycle that allows the CPU to execute a process 
            while iTerminadas < instrucciones:

                with self.__CentralProcessingUnit.request() as request:
                    yield request
                    #If the conditions are less than the speed, then, the number of instructions
                    #equals the speed it takes.
                    if (instrucciones - iTerminadas) >= speed:
                        nInstrucciones = speed
                    else:
                        #If it doesn't go with the conditions, it reduces the number
                        #of instructions with the ones already finished
                        nInstrucciones = (instrucciones - iTerminadas)

                    print(f"El CPU se encuenta ejecutando {nInstrucciones} instrucciones.")
                    yield self.__ENVIRONMENT.timeout(nInstrucciones/speed)
                    #Finished instructions are finished
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
            #The ram used by the simulation is showed
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
    #Function for the memory
    def memory(self):
        return self.eventmemory
    #Function for instructions
    def instructions(self):
        return self.eventinstructions
    #Function to show it finished
    def terminar(self):
        return self.eventinstructions<= 0
        numer = 0

 

