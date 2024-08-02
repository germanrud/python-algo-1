from queue import Queue as Cola

#1) ExactaBank


def copiar_cola_sin_modificarla(c:Cola) -> Cola:
    copia_cola:Cola = Cola()
    cola_aux:Cola = Cola()
    while not c.empty():
        elem = c.get()
        cola_aux.put(elem)
    while not cola_aux.empty():
        elto = cola_aux.get()
        copia_cola.put(elto)
        c.put(elto)
    return copia_cola



def reordenar_cola_priorizando_vips(fila_clientes:Cola[tuple[str,str]]) -> Cola[str]:
    copia_fila_clientes:Cola = copiar_cola_sin_modificarla(fila_clientes)
    fila_vip:Cola = Cola()
    fila_comun:Cola = Cola()
    res:Cola = Cola()
    while not copia_fila_clientes.empty():
        elemento:tuple[str,str] = copia_fila_clientes.get()
        if elemento[1] == "vip":
            fila_vip.put(elemento[0])
        else:
            fila_comun.put(elemento[0])
    while not fila_vip.empty():
        elto_vip:str = fila_vip.get()  #aca pifie puse mal el tipo en el parcial, puse tuple[str,str]
        res.put(elto_vip) 
    while not fila_comun.empty():
        elto:str = fila_comun.get()
        res.put(elto)
    return res

#--

def cuantos_puntos_obtuvo_el_competidor(estrategias:dict[str,str], competidor:str) -> int:
    suma:int = 0
    estrategia_competidor:str = estrategias[competidor]
    for rival in estrategias.keys():
        if rival != competidor:
            if estrategia_competidor == "me desvio siempre" and estrategias[rival] == "me desvio siempre":
                suma = suma - 10
            if estrategia_competidor == "me desvio siempre" and estrategias[rival] == "me la banco y no me desvio":
                suma = suma - 15
            if estrategia_competidor == "me la banco y no me desvio" and estrategias[rival] == "me desvio siempre":
                suma = suma - 5
            if estrategia_competidor == "me la banco y no me desvio" and estrategias[rival] == "me la banco y no me desvio":
                suma = suma + 10

def torneo_de_gallinas(estrategias:dict[str,str]) -> dict[str,int]:
    res:dict = dict()
    for competidor in estrategias.keys():
        res[competidor] = cuantos_puntos_obtuvo_el_competidor(estrategias, competidor)
        return res

#--

def obtener_columna_j_esima(tablero:list[list[str]], j:int) -> str:
    columna:str = []
    for fila in tablero:
        columna = columna + [fila[j]]
    return columna

tablero = [['X','O','O','X','X'],['X','O','O','X','X'],['X','O','O','X','X'],['X','O','O','X','X'],['X','O','O','X','X']]

print(obtener_columna_j_esima(tablero, 0))
          

