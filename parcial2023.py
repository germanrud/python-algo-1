
def acomodar(s:list[str]) -> list[int]:
    lista_UP:list[str] = []
    lista_LLA:list[str] = []
    for i in range(len(s)):
        if s[i] == "UP":
            lista_UP = lista_UP + [s[i]]
        else:
            lista_LLA = lista_LLA + [s[i]]
    lista_conjunta = lista_UP + lista_LLA
    return lista_conjunta


#lista = ["LLA","UP","UP","LLA","LLA","LLA","UP","LLA","UP","UP"]

#--

def pos_umbral(s:list[int], u:int) -> int:
    umbral:int = u
    gente_ingresada:int = 0
    res:int = -1
    for i in range(len(s)):
        if s[i]>=0:
            gente_ingresada = gente_ingresada + s[i]
        if gente_ingresada > u:
            res = i
            return res
    return res

#lista_rest = [2,3,-3,-5,3,-4,2]

#--

def se_cumple_para_una_fila(s:list[int]) -> bool:
    estado:bool = True
    mitad:int = int(len(s)/2)
    for i in range(mitad):
        if s[i]!=s[i+mitad]:
            estado = False
    return estado


def columnas_repetidas(mat:list[list[int]]) -> bool:
    estado = True
    for i in range(len(mat)):
        if not (se_cumple_para_una_fila(mat[i])):
            estado = False
    return estado

#esta forma sirve si estoy convecido que la condicion de que para cada fila sea siemtrica respecto de la mitad es cond suficiente.
#para probar, otra forma mas larga seria, convirtiendo la lista, en lista de columnas y ver si ahi la lista es simetrica respecto de la mitad



def obtener_col_k_esima(mat:list[list[int]],k:int) -> list[int]:
    columna:list[int] = []
    for i in range(len(mat)):
        columna.append(mat[i][k])
    return columna



def convertir_lista_de_filas_en_lista_de_columnas(mat:list[list[int]]) -> list[list[int]]:
    nueva_lista_de_cols:list[list[int]] = []
    for i in range(len(mat[0])):
        nueva_lista_de_cols.append(obtener_col_k_esima(mat,i))
    return nueva_lista_de_cols


def columnas_repetidas2(mat:list[list[int]]) -> bool:
    estado = True
    columnas_matriz:list[list[int]] = convertir_lista_de_filas_en_lista_de_columnas(mat)
    mitad:int = int(len(columnas_matriz)/2)
    for i in range(mitad):
        if columnas_matriz[i]!=columnas_matriz[i+mitad]:
            estado = False
    return estado

matriz = [[1,2,1,2],[-5,6,-5,6],[0,1,0,1],[23,12,23,12]]

print(matriz)

#--

