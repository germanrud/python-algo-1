def acomodar(s:list[str]) -> list[str]:
    lista_UP:list[str] = []
    lista_LLA:list[str] = []
    for i in range(len(s)):
        if s[i] == 'UP':
            lista_UP.append(s[i])
        else:
            lista_LLA.append(s[i])
    lista_junta:list[str] = lista_UP + lista_LLA
    return lista_junta

#--

def pos_umbral(s:list[int], u:int) -> int:
    suma_pos:int = 0
    res:int = -1
    for i in range(len(s)):
        if s[i]>=0:
            suma_pos = suma_pos + s[i]
        if suma_pos>u and res<0:
            res = i
    return res


#--

def fila_sym_respecto_de_la_mitad(s:list[int]) -> bool:   #req: |x| par para todo x e S
    estado:bool = True
    mitad_longitud:int = int(len(s)/2)
    for i in range(0,mitad_longitud):
        if s[i]!=s[i + mitad_longitud]:
            estado = False
    return estado


def columnas_repetidas(m:list[list[int]]) -> bool:
    estado = True
    for fila in m:
        if not (fila_sym_respecto_de_la_mitad(fila)):
            estado = False
    return estado

#--

def cuantas_veces_quedo_en_la_pos_i_una_nacion(nacion:str, torneos:dict[int, list[str]], i:int) -> int:
    contador:int = 0
    for anio in torneos.keys():
        if  torneos[anio][i] == nacion:
            contador = contador + 1
    return contador
    

def lista_posiciones_nacion(nacion:str, naciones:list[str], torneos:dict[int, list[str]]) -> list[int]:
    lista_vacia:list[int] = []
    for i in range(len(naciones)):
        lista_vacia.append(cuantas_veces_quedo_en_la_pos_i_una_nacion(nacion, torneos, i))
    return lista_vacia


def cuenta_posiciones_por_nacion(naciones:list[str], torneos:dict[int, list[str]]) -> dict[str, list[int]]:
    res:dict = dict()
    for nacion in naciones:
        res[nacion] = lista_posiciones_nacion(nacion, naciones, torneos)
    return res


naciones= ["arg", "aus", "nz", "sud"]
torneos = {2023:["nz", "sud", "arg", "aus"], 2022:["nz", "sud", "aus", "arg"], 2021:["nz", "aus", "sud", "arg"]}

print(cuenta_posiciones_por_nacion(naciones, torneos))
