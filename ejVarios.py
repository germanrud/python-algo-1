from queue import LifoQueue as Pila
from queue import Queue as Cola
import numpy as np
import random

#parcial integrador 2023

def codificar(b:list[(str,str)], c:str) -> str:
    nueva_lista:str = []
    for i in range(len(c)):
        for j in range(len(b)):
            if c[i]==b[j][0]:
                nueva_lista = nueva_lista + [b[j][1]]
    return nueva_lista
'''
b = [("a","b"),("g","r"),("k","z"),("c","t"),("s","a")]

c = "gaks"

print(codificar(b,c))
'''
#-- descomponer en primos

def divisores_propios_de_un_numero(n:int) -> list[int]:
    lista_divisores:list[int] = []
    for i in range(2,n):
        if n%i == 0:
            lista_divisores.append(i)
    return lista_divisores


def es_primo(n:int) -> bool:
    estado:bool = False
    if divisores_propios_de_un_numero(n) == []:
        estado = True
    return estado


def descomponer_en_primos(n:int) -> list[int]:
    numero:int = n
    lista_vacia:list[int] = []
    i:int = 2
    while n!=1:
        if es_primo(i) and n%i == 0:
            while n%i == 0:
                lista_vacia.append(i)
                n = n/i
        i = i+1
    return lista_vacia

'''
fichero = open("~/archivo.txt","r")
print(fichero.read())

''

'''
def prueba_sin_modificar_la_original(s:list[int]) -> list[int]:
    x = s.copy()
    for i in range(len(x)):
        x[i] = x[i]+1
    return x

def prueba_modificando_la_original_sin_querer(s:list[int]) -> list[int]:
    x = s
    for i in range(len(x)):
        x[i] = x[i]+1
    return x




def prueba(s:list[int]) -> list[int]:
    lista_nueva = []
    for i in range(len(s)):
        elemento = lista_nueva.append(s[i] +1)
    return lista_nueva



def maximo(s:list[int]) -> int:
    max:int
    for i in range(len(s)):
        if i==0:
            max = s[i]
        if s[i]>max:
            max = s[i]
    return max


def pruebita(s:list) -> list:
    lista_nueva = []
    for i in range(len(s)):
        if s[i] >=2:
            lista_nueva.append(s[i])
        if s[i]<=0:
            lista_nueva.append(s[i] + 10)
    return lista_nueva

def pruebita_elif(s:list) -> list:
    lista_nueva = []
    for i in range(len(s)):
        if s[i] >=2:
            lista_nueva.append(s[i])
        elif s[i]<=0:
            lista_nueva.append(s[i] + 10)
    return lista_nueva



def pruebita_elif1(x:int):   #asi mete solo en una
    lista_nueva1 = []
    lista_nueva2 = []
    if x>3:
        lista_nueva1.append(x)
    else:
        if x>10:
            lista_nueva2.append(x)
    print(lista_nueva1)
    print(lista_nueva2)

def pruebita_elif2(x:int):   #creo que es lo mismo que la 1
    lista_nueva1 = []
    lista_nueva2 = []
    if x>3:
        lista_nueva1.append(x)
    elif x>10:
        lista_nueva2.append(x)
    print(lista_nueva1)
    print(lista_nueva2)

def pruebita_elif2(x:int):  #asi mete en las dos listas
    lista_nueva1 = []
    lista_nueva2 = []
    if x>3:
        lista_nueva1.append(x)
    if x>10:
        lista_nueva2.append(x)
    print(lista_nueva1)
    print(lista_nueva2)

def pertenece_elto_a_lista_str(s:list[str],x:str) -> bool:
    estado:bool = False
    for i in range(len(s)):
        if s[i] == x:
            estado = True
    return estado

def armar_dicc(x) -> dict:
    d:dict = dict()
    for i in range(x):
        d[i] = i
    return d

dicc = armar_dicc(3)

def crear_lista_de_claves(dict:dict) -> list:
    lista_nueva = []
    for c in dict.keys():
        lista_nueva.append(c)
    return lista_nueva
   
#pila

def armar_pila_a_partir_de_lista(s:list) -> Pila:
    pila:Pila = Pila()
    for i in range(len(s)):
        pila.put(s[i])
    return pila


def mostrar_eltos_pila(p:Pila) -> None:
    copia_pila:Pila = Pila()
    while not p.empty():
        elem = p.get()
        print("a la ida :",elem)
        copia_pila.put(elem)
    while not copia_pila.empty():
        elto = copia_pila.get()
        p.put(elto)
    

def copiar_pila_sin_modificar_la_original(p:Pila) -> Pila:
    copia_pila_res:Pila = Pila()
    pila_auxiliar:Pila = Pila()
    while not p.empty():
        elem = p.get()
        pila_auxiliar.put(elem)
    while not pila_auxiliar.empty():
        elto = pila_auxiliar.get()
        copia_pila_res.put(elto)
        p.put(elto)
    return copia_pila_res



lista = [1,2,3,4]
pilita = armar_pila_a_partir_de_lista(lista)

copia = copiar_pila_sin_modificar_la_original(pilita)

print(pilita.queue)
print(copia.queue)


#cola
def reverso(s:list) -> list:
    lista_nueva:list = []
    for i in range(len(s)-1,-1,-1):
        lista_nueva.append(s[i])
    return lista_nueva

def armar_cola_a_partir_de_lista(s:list) -> Cola:
    cola:Cola = Cola()
    for i in range(len(s)):
        cola.put(s[i])
    return cola


def mostrar_eltos_cola(c:Cola) -> None:
    copia_cola:Cola = Cola()
    lista_colita = []
    while not c.empty():
        elem = c.get()
        lista_colita.append(elem)
        copia_cola.put(elem)
    while not copia_cola.empty():
        elto = copia_cola.get()
        c.put(elto)
    print("la fila mirando a la derecha queda: ", reverso(lista_colita))


def copiar_cola_sin_modificar_la_original(c:Cola) -> Cola:
    res:Cola = Cola()
    auxiliar:Cola = Cola()
    while not c.empty():
        elem = c.get()
        auxiliar.put(elem)
    while not auxiliar.empty():
        elto = auxiliar.get()
        c.put(elto)
        res.put(elto)
    return res

def copiar_cola_sin_modificarla(c:Cola) -> Cola: #copia una cola sin modificar la original
    cola_res:Cola = Cola()
    cola_auxiliar:Cola = Cola()
    while not c.empty():
        elem:int = c.get()
        cola_auxiliar.put(elem)
        cola_res.put(elem)
    while not cola_auxiliar.empty():
        c.put(cola_auxiliar.get())
    return cola_res
'''
lista = [1,2,3,4]

colita = armar_cola_a_partir_de_lista(lista)

mostrar_eltos_cola(colita)

copia_colita = copiar_cola_sin_modificar_la_original(colita)

print("la copia queda :")
mostrar_eltos_cola(copia_colita)
print(colita.queue)


mostrar_eltos_cola(colita)
'''