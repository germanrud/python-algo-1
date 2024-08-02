from queue import Queue as Cola

def copiar_cola(c:Cola) -> Cola:
    res:Cola = Cola()
    cola_aux:Cola = Cola()
    while not c.empty():
        elem = c.get()
        cola_aux.put(elem)
    while not cola_aux.empty():
        elto = cola_aux.get()
        res.put(elto)
        c.put(elto)
    return res

def orden_de_atencion(urgentes:Cola[int], postergables:Cola[int]) -> Cola[int]:
    copia_urgentes:Cola[int]  = copiar_cola(urgentes)
    copia_postergables:Cola[int] = copiar_cola(postergables)
    res:Cola[int] = Cola()
    while not copia_urgentes.empty():
        elto_urgente:int = copia_urgentes.get()
        elto_postergable:int = copia_postergables.get()
        res.put(elto_urgente)
        res.put(elto_postergable)
    return res


def armar_colita(s:list) -> Cola:
    res:Cola  = Cola()
    for i in range(len(s)):
        res.put(s[i])
    return res

def mostrar_cola(c:Cola):
    copia = copiar_cola(c)
    while not copia.empty():
        elto = copia.get()
        print(elto)

'''
colita_urg = armar_colita([1,2,3,4,5])
colita_pos = armar_colita([7,9,11,344,88])


cola_hos = orden_de_atencion(colita_urg, colita_pos)

mostrar_cola(cola_hos)
'''

def cantidad_veces_aparece(registros: list[tuple[int, str]], enfermedad:str) -> int:
    res:int = 0
    for i in range(len(registros)):
        if registros[i][1] == enfermedad:
            res = res + 1
    return res


def porcentaje_enfermedad(registros: list[tuple[int, str]], enfermedad:str) -> float:
    res:float = cantidad_veces_aparece(registros, enfermedad)/len(registros)
    return res

def alarma_epidemeologica(registros: list[tuple[int, str]], infecciosas:list[str], umbral:float) -> dict[tuple[str, float]]:
    res:dict = dict()
    for enfermedad in infecciosas:
        proporcion:float = porcentaje_enfermedad(registros, enfermedad)
        if proporcion >= umbral:
            res[enfermedad] = proporcion
    return res

'''
regs = [(123,"cancer"), (456,"varicela"), (789,"sifilis"), (22,"sifilis"), (334,"cancer")]

print(alarma_epidemeologica(regs, ["sifilis", "cancer"], 0.2))
'''

def suma(s:list[int]) -> int:
    res:int = 0
    for i in range(len(s)):
        res = res + s[i]
    return res

def maximo_entre_listas(horas: dict[int, list[int]]) -> int:
    res:int = 0
    for id in horas.keys():
        cant_horas:int = suma(horas[id])
        if cant_horas >= res:
            res = cant_horas
    return res


def empleados_del_mes(horas: dict[int, list[int]]) -> list[int]:
    res: list[int] = []
    for id in horas.keys():
        if suma(horas[id]) == maximo_entre_listas(horas):
            res.append(id)
    return res

'''
horas = {1:[1,2,72], 2:[3,2,1,1,3,5], 3:[5,34,2,2],4:[3,2,1],5:[9,33,1], 6:[2,3,4,5,3,2,23,4,5,6,6,6,6],7:[75]}
print(empleados_del_mes(horas))
'''

def proporcion_camas_ocupadas(piso:list[bool]) -> float:
    cant_camas_ocupadas:int = 0
    for i in range(len(piso)):
        if piso[i] == True:
            cant_camas_ocupadas = cant_camas_ocupadas + 1
    res: float = cant_camas_ocupadas/len(piso)
    return res


def nivel_de_ocupacion(camas_por_piso:list[list[bool]]) -> list[float]:
    res: list[float] = []
    for i in range(len(camas_por_piso)):
        res.append(proporcion_camas_ocupadas(camas_por_piso[i]))
    return res


camas_por_piso = [[True,False,False,True], [False,False,False,False], [True,False,False,False], [True,True,False,True] ]

print(nivel_de_ocupacion(camas_por_piso))