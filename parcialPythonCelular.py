
def verificar_transacciones(s:str) -> int:
    saldo:int = 0
    i:int = 0
    while i<len(s) and s[i]!='x' and saldo>=0:
        if s[i] == 'r':
            saldo = saldo + 350
        if s[i] == 'v':
            saldo = saldo - 56
            if saldo<0:
                return saldo + 56   # vale esto???
        i = i+1
    return saldo



def verificar_transacciones2(s:str) -> int:   #creo que bien
    saldo:int = 0
    i:int = 0
    while i<len(s) and s[i]!='x' and (not (saldo<56 and s[i]=='v')):
        if s[i] == 'r':
            saldo = saldo + 350
        if s[i] == 'v':
            saldo = saldo - 56
        i = i+1
    return saldo

'''
programa = "ssrvvvvvvvvvvvv"

print(verificar_transacciones(programa))
'''

def valor_minimo(s:list[(float,float)]) -> float:
    minimo:float = s[0][0]
    for i in range(len(s)):
        if s[i][0]<= minimo:
            minimo = s[i][0]
    return minimo

'''
s = [(1.0, 5.2), (10.4, 15.1), (19.7, 28.9), (25.4, 35.6), (-3.1, 1.3)]

print(valor_minimo(s))
'''

def maximo_para_cada_empresa(s:list[(int, float)]) -> float:
    maximo:float = s[0][1]
    for i in range(len(s)):
        if s[i][1]>= maximo:
            maximo = s[i][1]
    return maximo

def minimo_para_cada_empresa(s:list[(int, float)]) -> float:
    minimo:float = s[0][1]
    for i in range(len(s)):
        if s[i][1]<= minimo:
            minimo = s[i][1]
    return minimo


def valores_extremos(cotizaciones_diarias:dict[str,list[(int, float)]]) -> dict:
    res:dict = dict()
    for empresa in cotizaciones_diarias.keys():
        res[empresa] = (minimo_para_cada_empresa(cotizaciones_diarias[empresa]), maximo_para_cada_empresa(cotizaciones_diarias[empresa]))
    return res

def valores_extremos_otra_forma(cotizaciones_diarias:dict[str,list[(int, float)]]) -> dict:
    res:dict = dict()
    for empresa, valores in cotizaciones_diarias.items():
        res[empresa] = (minimo_para_cada_empresa(valores), maximo_para_cada_empresa(valores))
    return res

'''
cotizaciones_diarias = {"YPF" : [(1,10),(15, 3), (31,100)], "ALUA" : [(1,0), (20, 50), (31,30)]}

print(valores_extremos(cotizaciones_diarias))
'''
#--

def pertenece(s:list[int],x:int) -> bool:
    estado:bool = False
    for i in range(len(s)):
        if s[i]==x:
            estado = True
    return estado


def no_hay_repes_s0(s:list[int]) -> bool:
    estado:bool = True
    eltos_de_s:list[int] = []
    for i in range(len(s)):
        if pertenece(eltos_de_s,s[i]):
            estado = False
        if s[i] != 0:
            eltos_de_s.append(s[i])
    return estado


def armar_lista_de_columnas(m:list[list[int]]) -> list[list[int]]:
    nueva_matriz:list[list[int]] = list()
    for i in range(len(m)):
        columna_i_esima:list[int] = []
        for j in range(len(m)):
            columna_i_esima.append(m[j][i])
        nueva_matriz.append(columna_i_esima)
    return nueva_matriz



def es_sudoku_valido(m:list[list[int]]) -> bool:
    estado:bool = True
    m_tr:list[list[int]] = armar_lista_de_columnas(m)
    for i in range(len(m)):
        if not(no_hay_repes_s0(m[i]) and no_hay_repes_s0(m_tr[i])):
            estado = False
    return estado

matriz_fila_1_distinta = [list(range(1,10))] + [[0]*9]*8

mat_prueba =  [
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[9, 8, 7, 6, 4, 5, 3, 2, 1],
[0, 2, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 4, 0, 0, 0],
[0, 0, 0, 0, 6, 0, 0, 0, 0],
[0, 0, 0, 5, 0, 0, 0, 0, 0],
[0, 0, 4, 0, 0, 0, 0, 0, 0],
[0, 3, 0, 0, 0, 0, 0, 0, 0],
[2, 0, 0, 0, 0, 0, 0, 0, 0]
]


print(es_sudoku_valido(mat_prueba))



