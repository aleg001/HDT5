#ImplementacionCola.py
#Universidad del Valle de Guatemala
#Alejandro Gómez 20347
#Gabriela Contreras 20213
#Creacion: 8-03-21
#Ultima Edicion: 8-03-21




def __init__(self):
    self.__list=[]

def add_stack(self, object):
    self.__list.append(object)

def empty_stack(self):
    if len(self.__list)== 0:
        XD = True
        return XD
    else:
        XD = False
        return False

def count_stack(self):
    return len(self.__list)


def pop_stack(self):
    if self.empty():
        print ("Vacio bro")
    else :
        self.cola=(self.cola[i]for i in range (1,self.size))
        self.size -=1


def push_stack(self,dato):
    if self.empty():
        print ("Vacio xd")
    else:
        self.cola= (self.cola[i] for i in range(1,self.size))


def peek_stack(self):
    if self.empty():
        return None  
    else:
        return self.__list[0]