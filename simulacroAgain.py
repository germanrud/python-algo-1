def ultima_aparicion(s:list[int], x:int) -> int:
    res:int = 0
    for i in range(len(s)):
        if s[i] == x:
            res = i
    return res

#--

def pertenece(s:list[int],x:int) -> bool:
    estado:bool = False
    for i in range(len(s)):
        if s[i]==x:
            estado = True
    return estado

def elementos_de_la_primera_que_no_estan_en_la_segunda(s1:list[int], s2:list[int]) -> list[int]:
    lista_nueva:list[int] = []
    for i in range(len(s1)):
        if ((not(pertenece (s2,s1[i]))) and (not(pertenece(lista_nueva, s1[i])))):
            lista_nueva.append(s1[i])
    return lista_nueva


def elementos_exclusivos(s1:list[int], s2:list[int]) -> list[int]:
    res:list[int] = elementos_de_la_primera_que_no_estan_en_la_segunda(s1,s2) + elementos_de_la_primera_que_no_estan_en_la_segunda(s2,s1)
    return res

#--

def contar_traducciones_iguales(ing:dict[(str,str)], ale:dict[str,str]) -> int:
    contador:int = 0
    for clave in ing.keys():
        if clave in ale:
            if ing[clave] == ale[clave]:
                contador = contador + 1
    return contador

'''
aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
ingles = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}

print(contar_traducciones_iguales(ingles,aleman))
'''

#--

def cuantas_veces_aparece(s:list[int], x:int) -> int:
    contador:int = 0
    for i in range(len(s)):
        if s[i]==x:
            contador = contador + 1
    return contador


def lista_sin_repeticion(s:list[int]) -> list[int]:
    lista_nueva:list[int] = []
    for i in range(len(s)):
        if not(pertenece(lista_nueva, s[i])):
            lista_nueva.append(s[i])
    return lista_nueva


def convertir_a_diccionario(s:list[int]) -> dict[int,int]:
    lista_sin_repetidos:list[int] = lista_sin_repeticion(s)
    res:dict[int,int] = dict()
    for i in range(len(lista_sin_repetidos)):
        res[lista_sin_repetidos[i]] = cuantas_veces_aparece(s, lista_sin_repetidos[i])
    return res


lista = [-1, 0, 4, 100, 100, -1, -1]

dicc = convertir_a_diccionario(lista)
print(dicc)
