#Main.py
#Universidad del Valle de Guatemala
#Alejandro Gómez 20347
#Gabriela Contreras 20213
#Creacion: 7-03-21
#Ultima Edicion: 9-03-21

import simpy 
import random 
from time import sleep
import sys
import Menu as mn
import Event as event 


#Attributes 
opcion=0
var = False
mn.menu()

#Cicle of the program 
while var == False:
    #Defensive program for an input
    try:
        mn.Bienvenida()
        opcion= input("\n",'\033[4m',"Elija la opcion que quiera: ",'\033[m')
        opcion= int(opcion)

    except ValueError:
        mn.Error()

# Availabe Operations  
    if opcion == 1:
        mn.Iniciar()
        mn.menu()
    
    if opcion == 2:
        print("\n")
        mn.menu()

    if opcion == 3:
        mn.menu()

    if opcion == 4:
        mn.menu()

    if opcion == 5:
        mn.menu()

    if opcion == 6:
        print("\n")
        mn.menu()
        mn.Creditos()

    if opcion == 7:
        print("\n")
        mn.Salida()
        var = True #breaks cicle 





