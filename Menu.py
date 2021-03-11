#Menu.py
#Universidad del Valle de Guatemala
#Alejandro Gómez 20347
#Gabriela Contreras 20213
#Creacion: 7-03-21
#Ultima Edicion: 11-03-21

#Imports  for the functions 
from time import sleep
import sys
import Event
import statistics
import simpy
import random

# Function that gives the welcome to the user 
def Bienvenida():
    Oraciones = "Bienvenido al simulador de programa"
    for char in Oraciones:
        sleep(0.005)
        sys.stdout.write(char)
        
#Function that contains the menu
def menu():
    print("\n",'\033[4m]',"SIMULADOR",'\033[m',"\n")
    print (" 1. Iniciar Simulacion", "\n","2.Creditos","\n","3.Salir")

#Function that contains the credits of the people that ralized the program 
def Creditos():
    print("Creado por:")
    print("Alejandro Gomez")
    print("Paola Contreras")

#Funticon that say goodbye to the user 
def Salida():
    print("Saliendo el programa...")
    print("Gracias por utilizar nuestro programa jeje")

#Function that shows an error 
def Error():
    print("Ocurrio un error, unicamente se aceptan numeros enteros")

#Function that contains the simulation start message
def Iniciar():
    print("Iniciando simulacion...")