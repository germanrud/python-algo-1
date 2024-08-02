import random


def crear_todas_las_cartas() -> dict[int, (str,str,int,str)]:
    shape:list[str] = ["ovals", "squigles", "diamonds"]
    color:list[str] = ["red", "purple", "green"]
    shading:list[str] = ["solid", "striped", "outlined"]


    res:dict[int, (str,str,int,str)] = dict()
    i:int = 1
    for forma in shape:
        for col in color:
            for num in range (1,4):
                for relleno in shading:
                    res[i] = (forma, col, num, relleno)
                    i = i + 1
    return res


def elegir_cartas_de_la_mesa(cartas:dict) -> list[(str,str,int,str)]:

    lista_nums:list[int] = []
    for i in range(1,82):
        lista_nums.append(i)

    res:list[(str,str,int,str)] = []
    for i in range(12):
        numero_elegido:int = random.choice(lista_nums)
        carta:tuple[str,str,int,str] = cartas[numero_elegido]
        res.append(carta)
        lista_nums.remove(numero_elegido)
    return res


def coinciden_en_esta_categoria(s:list[str]) -> bool:
    res:bool = False
    if s[0] == s[1] and s[0] == s[2]:
        res = True
    if s[0] != s[1] and s[0] != s[2] and s[1] != s[2]:
        res = True
    return res


def es_set(trio:list[(str,str,int,str)]) -> bool:
    estado:bool = True
    for i in range(4):
        lista = [trio[0][i], trio[1][i], trio[2][i]]
        if not coinciden_en_esta_categoria(lista):
            estado = False
    return estado


def todos_los_trios(s:list) -> list[list]:
    res:list[list] = []
    copia_lista = s.copy()
    long = len(copia_lista)

    for i in range(long - 2):
        primer_fija = copia_lista.pop(0)

        lista_aux = copia_lista.copy()
        for j in range(len(lista_aux)):
            segunda_fija = lista_aux.pop(0)

            for k in range(len(lista_aux)):
                la_que_itera = lista_aux[k]
                trio = ((primer_fija, segunda_fija, la_que_itera))
                res.append(trio)
    
    return res



def sets_de_la_mesa(mesa:list[(str,str,int,str)]) -> list[list[(str,str,int,str)]]:
    res = []
    trios = todos_los_trios(mesa)
    for tri in trios:
        if es_set(tri):
            res.append(tri)
    return res



mesa = elegir_cartas_de_la_mesa(crear_todas_las_cartas())

print("mesa:" , mesa)
print("hay " ,len(sets_de_la_mesa(mesa)), "sets, " )
print("los sets de la mesa: ", sets_de_la_mesa(mesa))










    


