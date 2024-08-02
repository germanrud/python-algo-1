import random
import numpy as np # type: ignore

def pertenece(lista:list[int], x:int) -> bool:
    indice = 0
    while indice < len(lista):
        if lista[indice] == x:
            return True
        indice = indice + 1
    return False


# para ver el tipo es type(x) en la consola

def perteneceProfe(s:list[int], x:int) -> bool:
    res: bool = False
    for i in range(len(s)):
        if s[i]==x:
            res = True
    return res

def perteneceProfeWhile(s:list[int], x:int) -> bool:
    res: bool = False
    i: int = 0
    longitud_lista = len(s)
    while i <= longitud_lista:
        if s[i] == x:
            res = True
        i = i + 1
    return res



def pertenece_count(lista:list, x:int):
    if list.count(x)==0:
        return True
    else:
        return False

def perteneceChar(lista:str, x:chr) -> bool:
    indice = 0
    while indice < len(lista):
        if lista[indice] == x:
            return True
        indice = indice + 1
    return False


def perteneceFor(lista:list, x:int) -> bool:
    for i in range(len(lista)):
        if lista[i] == x:
            return True
    return False

def perteneceFor2(lista:list, x:int) -> bool:
    for y in lista:
        if x==y:
            return True
    return False


def perteneceSimple(lista:list, x:int) -> bool:
    if x in lista:
        return True
    else:
        return False


#--

def divide_a_todos(lista:list[int], x:int) -> bool:
    for i in range(len(lista)):
        if lista[i]%x !=0:
            return False
    return True

def divideATodos(lista:list[int], x:int) -> bool:
    for elem in lista:
        if elem%x !=0:
            return False
    return True


#--

def suma_total(s:list[int]) -> int:
    res: int = 0
    for i in range(0,len(s),1):
        res = res + s[i]
    return res

def suma_total_while(s:list[int]) -> int:
    i = 0
    suma = 0
    while i<len(s):
        suma = suma + s[i]
        i = i+1
    return(suma)

def sumaTotalFor(s:list[int]) -> int:
    suma = 0
    for i in range(len(s)):
        suma = suma + s[i]
    return(suma)

def sumaTotalFor2(s:list[int]) -> int:
    suma = 0
    for elem in s:
        suma = suma + elem
    return(suma)
'''
#sumar 3 a cada a elto de la lista
def suma3(s:list) -> None:
    for i in range(len(s)):
        s[i] = s[i]+3

pigi:list[int] = [1,2,3]
print("al pirnicpio es " , pigi)
suma3(pigi)
print(pigi)
'''
#--

def ordenados(s:list[int]) -> bool:
    for i in range(len(s)-1):
        if s[i]>=s[i+1]:
            return False
    return True

def ordenados2(s:list[int]) -> bool:
    indice = 0
    while indice < (len(s)-1):
        if s[indice]>=s[indice + 1]:
            return False
        indice = indice + 1
    return True

#--

def longitudMayorA7(s:list[str]) -> bool:
    for i in range(len(s)):
        print(len(s[i]))
        if len(s[i])>7:
            return True
    return False

#--

def borrar_espacios(frase:str) -> str:  
    while frase.count(" ")>0:
        frase.remove(" ")
    return frase



def borrarEspacios(frase:str) -> str:
    lienzo = ""
    contador = 0
    while contador<len(frase):
        if frase[contador] != ' ':
            lienzo = lienzo + frase[contador]
            contador = contador + 1
        else:
            contador = contador + 1
    return(lienzo)

def reverso(l:list) -> list:
    lienzo = []
    for i in range(len(l)):
        lienzo = lienzo + [l[-(i+1)]]
    return(lienzo)

def es_palindromo(frase:str) -> bool:     
    a = frase.lower()
    if borrarEspacios(a) == borrarEspacios(reverso(a)):
        return True
    else:
        return False

#--

def al_menos_una_mayuscula (s:str) -> bool:
    estado: bool = False
    i: int = 0
    while i<len(s):
        if s[i]>='A' and s[i]<='Z':
            estado = True
        i = i+1
    return estado


def alMenosUnaMay (s:str) -> bool:    #otra forma
    estado: bool = False
    i: int = 0
    while i<len(s) and (not (s[i]>='A' and s[i]<='Z')):
        i = i+1
    estado = i<len(s)
    return estado


def al_menos_un_num (s:str) -> bool:
    estado: bool = False
    i: int = 0
    while i<len(s):
        if s[i]>='0' and s[i]<='9':
            estado = True
        i = i+1
    return estado

def al_menos_una_minuscula (s:str) -> bool:
    estado: bool = False
    i: int = 0
    while i<len(s):
        if s[i]>='a' and s[i]<='z':
            estado = True
        i = i+1
    return estado


def contrasena(clave:str) -> str:
    if al_menos_un_num(clave) and al_menos_una_mayuscula(clave) and al_menos_una_minuscula(clave) and len(clave)>8:
        return "verde"
    if len(clave)<5:
        return "roja"
    return "amarilla"

#--

def saldo_actual(movimientos:list[(str,int)]) -> int:
    saldo = 0
    for i in range(len(movimientos)):
        if (movimientos[i])[0] == 'I':
            saldo = saldo + (movimientos[i])[1]
        else:
            saldo = saldo - (movimientos[i])[1]
    return saldo

#--

def tiene_3_vocales_distintas(palabra:str) -> bool:
    vocales_acumuladas:list = []
    for i in range(len(palabra)):
        if palabra[i]>='A' and palabra[i]<='Z' and (not(perteneceChar(vocales_acumuladas,palabra[i]))):
            vocales_acumuladas.append(palabra[i])
    return(len(vocales_acumuladas)>=3, vocales_acumuladas)


#-- segunda parte

def cero_en_pos_pares_inout(s:list[int]) -> list[int]:   #inout
    for i in range(0,len(s),2):
        s[i] = 0
    return s


def cero_en_pos_pares_in(s:list[int]) -> list[int]:  #in    esta asi esta bien hecha, no modifica el valor de s
    lista_nueva: list[int] = s.copy() #DUDA! si se puede usar s.copy() ??????????????????
    for i in range(0,len(s),2):
        lista_nueva[i] = 0
    return lista_nueva

def cero_en_pos_pares_in_experimento(s:list[int]) -> list[int]:  
    lista_nueva: list[int] = s  #ESTA NO FUNCA pq asi modifico el valor de s, en la de arriba no
    for i in range(0,len(s),2):
        lista_nueva[i] = 0
    return lista_nueva

def cero_en_pos_pares_in_otra_forma(s:list[int]) -> list[int]:  #work as intended
    lista_new: list[int] = []
    for i in range(len(s)):
        if i%2 == 0:
            lista_new.append(0)
        else:
            lista_new.append(s[i])
    return lista_new

#--
#DUDA!!
def sin_vocales_in(s:str) -> str: #ok, creo una lista nueva.. pero si me pidieran inout.. como borro los eltos? si no puedo usar .remove
    lista_nueva: str = ""          # IMPORTANTEEEEEE! nunca podria ser un tipo primitivo somo str o int, de inout pq son inmutables!!
    for i in range(len(s)):
        if not (s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
            lista_nueva = lista_nueva + s[i]
    return lista_nueva


def sin_vocales_otra_forma_NO_SIRVE(s:str) -> str:       #ESTO NO FUNCIONA, pq str no acepta los .append, .remove, etc
    lista_new: str = s.copy()
    for i in lista_new:
        if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            lista_new.remove(i)
    return lista_new

#--

def reemplaza_vocales_chr(s:list[chr]) -> list[chr]:  #esto si uso list characteres
    lista_nueva: list[chr] = s.copy()
    for i in range(len(s)):
        if lista_nueva[i] == 'a' or lista_nueva[i] == 'e' or lista_nueva[i] == 'i' or lista_nueva[i] == 'o' or lista_nueva[i] == 'u':
            lista_nueva[i] = '_'
    return lista_nueva


def reemplaza_vocales_str(s:str) -> str:  #esta OK 
    frase_nueva: str = ""
    for i in range(len(s)):
        if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
            frase_nueva = frase_nueva + "_"
        else:
            frase_nueva = frase_nueva + s[i]
    return frase_nueva


def reemplaza_vocales_str_otra_forma_queNO_SIRVE(s:str) -> str:  #NO FUNCA pues s.copy no va
    frase_nueva:str = s.copy()
    for i in range(len(s)):
        if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
            frase_nueva[i] = "_"
    return frase_nueva

#--

def da_vuelta_str(s:str) -> str:
    frase_nueva: str = ""
    for i in range(len(s)):
        frase_nueva = frase_nueva + s[len(s)-(i+1)]
    return frase_nueva

#print(da_vuelta_str("join the navy"))
#--

def eliminar_repetidos(s:chr) -> str:      #DUDA aca lo mismo que en sin_vocales, si me pidieran inout.. como se haria??
    frase_nueva: str = ""
    for i in range(len(s)):
        if not (pertenece(frase_nueva,s[i])):
            frase_nueva = frase_nueva + s[i]
    return frase_nueva


def eliminar_repetidos_while(s:str) -> str:
    frase_nueva: str = ""
    i = 0
    while i<len(s):
        if not (pertenece(frase_nueva,s[i])):
            frase_nueva = frase_nueva + s[i]
        i = i+1
    return frase_nueva

#--

def promedio(s:list[int]) -> float:
    return(suma_total(s)/len(s))

def son_todos_mayores_o_iguales_a_n(s:list[int],n:int) -> bool:
    estado: bool = True
    for i in range(len(s)):
        if s[i] < n:
            estado = False
    return estado

def aprobado(s:list[int]) -> int:
    estado = 3
    if son_todos_mayores_o_iguales_a_n(s,4):
        if promedio(s)>=7:
            estado = 1
        else:
            estado = 2
    return estado

#--

def estudiantes() -> list[str]:
    x = input("ingrese nombre estudiante : ")
    lista_vacia:list[str] = []
    while x!= "listo":
        lista_vacia.append(x)
        x = input("ingrese nombre estudiante : ")
    return lista_vacia

#--

def historial_monedero() -> list[(str,float)]:
    x = input("ingrese opercion a realizar: ")
    y = float(input("ingrese monto: "))
    lista_vacia: list[(str,float)] = []
    while x!="X":
        lista_vacia.append((x,y))
        x = input("ingrese opercion a realizar: ")
        if x!="X":
            y = float(input("ingrese monto: "))
    return lista_vacia

#--

def suma_sieteYmedio(s:list[int]) -> float:
    suma = 0
    for i in range(len(s)):
        if s[i]>=10:
            suma = suma + 0.5
        else:
            suma = suma + s[i]
    return suma


def siete_y_medio():
    cartas_posibles:list[int] = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,10,10,10,10,11,11,11,11,12,12,12,12]
    primer_carta:int = random.choice(cartas_posibles)
    print("su primer carta es: ", primer_carta)
    cartas_jugador:list[int] = []
    cartas_jugador.append(primer_carta)
    cartas_posibles.remove(primer_carta)
    x = input("planta o pide?: ")
    while x!="planta" and suma_sieteYmedio(cartas_jugador)< 7.5:
        carta_obtenida:int = random.choice(cartas_posibles)
        print("saco un: " , carta_obtenida)
        cartas_posibles.remove(carta_obtenida)
        cartas_jugador.append(carta_obtenida)
        print("su mano es: " , cartas_jugador)
        print("suman" , suma_sieteYmedio(cartas_jugador))
        if suma_sieteYmedio(cartas_jugador) > 7.5:
            print("perdio :( chotis ")
            return cartas_jugador
        if suma_sieteYmedio(cartas_jugador)==7.5:
            print("GANO!!!!")
            return cartas_jugador
        x = input("planta o pide?: ")

    print("te plantaste antes amargo, sumaste: " , suma_sieteYmedio(cartas_jugador))
    return cartas_jugador

#--

def pertenece_a_cada_uno_version_1(s:list[list[int]], x:int, res:list[bool]):   #esta sirve para ambas versiones, pero modifico el 
    res.clear()                                                                 # tamano de la lista de booleanos
    for i in range(len(s)):
        if pertenece(s[i],x):
            res.append(True)
        else:
            res.append(False)

def pertenece_no_funciona(s:list[list[int]], x:int, res:list[bool]):  #lo que hicimos en clase que es un error, ojo
    res = []
    res = [True,True,False,True]

s = [[1,2,3],[3,2,1],[3,4,5],[4,3,2]]
res = [True]

pertenece_no_funciona(s,2,res)

print(res)

#DUDA: se hace como arriba o sea tomando a res como un parametro de entrada SIII pq asi lo pide la especificacion

'''
lista_de_lista_de_enteros:list[list[int]] = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]
numerito:int = 2
lista_booleana:list[bool] = [True,False,False,True,False,False,True]

print("antes: ", lista_booleana)

pertenece_a_cada_uno_version_1_otra_forma_sin_clear(lista_de_lista_de_enteros, numerito, lista_booleana)

print("luego: ", lista_booleana)
'''
#--

def es_matriz(s:list[list[int]]) -> bool:
    estado:bool = True
    if len(s)==0:
        estado = False
    longitud_de_las_filas = len(s[0])
    if longitud_de_las_filas == 0:
        estado = False
    for i in range(1,len(s)):
        if len(s[i]) != longitud_de_las_filas:
            estado = False
    return estado

#--

def filas_ordenadas(m:list[list[int]], res:list[bool]):  #tmb podria hacer con res[i] = , para mantener el tamano original de res
    res.clear()
    for i in range(len(m)):
        if ordenados(m[i]):
            res.append(True)
        else:
            res.append(False)

'''
matrix:list[list[int]] = [[1,2,3],[5,66,7],[7,8,9],[3,6,3]]
lista_booleana:list[bool] = [True,False,False,True,False,False,True]
print("antes: ", lista_booleana)

filas_ordenadas(matrix,lista_booleana)

print("luego: ", lista_booleana)
'''
#--
'''
def elevar_matriz_cuadrada_de_tamano_d_al_cuadrado(d:int, matriz:list[list[int]]) -> list[list[int]]:
    matriz_elevada:list[list[int]] = matriz.copy()
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            for k in range(len(matriz)):
                matriz_elevada[i][j] = ((matriz[i])[k] * (matriz[k])[j])
    return matriz_elevada
'''

def multiplicar_una_fila_por_columna(fila:list[int] , columna:list[int]) -> int:
    rdo = 0
    for i in range(len(fila)):
        rdo = rdo + fila[i]*columna[i]
    return rdo

def obtener_columna_k_esima_a_partir_de_matriz(matriz:list[list[int]],k:int) -> list[int]:
    columna:list[int] = []
    for i in range(len(matriz)):
        columna.append(matriz[i][k])
    return columna


def multiplicar_una_matriz_por_si_misma(matriz:list[list[int]]) -> list[list[int]]:
    matriz_nueva = np.random.random((len(matriz),len(matriz)))
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz_nueva[i][j] = multiplicar_una_fila_por_columna(matriz[i],obtener_columna_k_esima_a_partir_de_matriz(matriz,j))
    return matriz_nueva


def multiplicar_una_matriz_por_otra(matriz1:list[list[int]], matriz2:list[list[int]]) -> list[list[int]]:
    matriz_new = np.random.random((len(matriz1),len(matriz2)))
    for i in range(len(matriz1)):
        for j in range(len(matriz2)):
            matriz_new[i][j] = multiplicar_una_fila_por_columna(matriz1[i],obtener_columna_k_esima_a_partir_de_matriz(matriz2,j))
    return matriz_new


def elevar_matriz_cuadrada_de_tamano_d_a_la_p(d:int, p:int) -> list[list[int]]:
    matriz:list[list[int]] = np.random.random((d,d))
    print(matriz)
    matriz_nueva = matriz      #si voy modificando matriz_nueva, se modifica matriz?
    for i in range(0,p-1):
        matriz_nueva = multiplicar_una_matriz_por_otra(matriz_nueva, matriz)
    return matriz_nueva







