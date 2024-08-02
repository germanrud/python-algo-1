
def ind_nesima_aparicion(s:list[int], n:int, elem:int) -> int:
    contador:int = 0
    for i in range(len(s)):
        if s[i]==elem:
            contador += 1
        if contador == n:
                return i
    if contador < n:
         return -1

#--

def mezclar(s1:list[int], s2:list[int]) -> list[int]:
    res:list[int] = []
    for i in range(len(s1)):
        res.append(s1[i])
        res.append(s2[i])
    return res

#--
def reverso(s:list[int]) -> list[int]:
    lista_nueva:list[int] = []
    for i in range(len(s)-1,-1,-1):
        lista_nueva.append(s[i])
    return lista_nueva


def es_capicua(s:list[int]) -> bool:
     return reverso(s) == s
     
def matriz_capicua(m:list[list[int]]) -> bool:
    estado:bool = True
    for i in range(len(m)):
         if (not (es_capicua(m[i]))):
              estado = False
    return estado


