from queue import LifoQueue as Pila
from queue import Queue as Cola

def armar_pila(s:list[int]) -> Pila:
    p:Pila = Pila()
    for i in range(len(s)):
        p.put(s[i])
    return p


def copiar_pila_sin_modificarla(p:Pila) -> Pila:
    pila_res:Pila = Pila()
    pila_aux:Pila = Pila()
    while not p.empty():
        elem:int = p.get()
        pila_aux.put(elem)
    while not pila_aux.empty():
        elto:int = pila_aux.get()
        p.put(elto)
        pila_res.put(elto)
    return pila_res


def mostrar_eltos_pila(p:Pila):
    copia_pila:Pila = copiar_pila_sin_modificarla(p)
    while not copia_pila.empty():
        elem:int = copia_pila.get()
        print(elem)
'''
lista = [1,2,3,4]
pilita = armar_pila(lista)

copia_pilita = copiar_pila_sin_modificarla(pilita)

mostrar_eltos_pila(pilita)
'''

dicc = dict()
dicc["uno"] = 1
dicc["dos"] = 2

print(dicc)

dicc.pop("uno")

print(dicc)