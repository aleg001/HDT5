import random as r

class Event:
    Memory=0;
    Instrucctions=0;
    Id=0;
    

def __init__(self,name,memory,instrctions):
    self.Id=name
    self.Memory=memory
    self.Instrctions= instrctions

def show(self):
    print ("Process", self.Id,"Memory",self.Memory)
