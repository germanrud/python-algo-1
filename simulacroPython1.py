# 1) problema ultima aparicion (s: seq<Z>, e:Z) : Z

def ultima_aparicion_opcion_recorriendo_para_atras (s:list[int], e:int) -> int:
    for i in range(len(s)-1,-1,-1):
        if s[i] == e:
            return i


def ultima_aparicion_mas_standard_for (s:list[int], e:int) -> int:
    res:int = 0
    for i in range(len(s)):
        if s[i] == e:
            res = i
    return res

def ultima_aparicion_while (s:list[int], e:int) -> int:
    res:int = 0
    i:int = 0
    while i<len(s):
        if s[i] == e:
            res = i
        i = i+1
    return res

#--
# 2) problema elementos exclusivos (s: seq<Z>, t: seq<Z>) : seq<Z>

def pertenece(s:list[int], x:int) -> bool:
    estado:bool = False
    for i in range(len(s)):
        if s[i] == x:
            estado = True
    return estado


def elementos_exclusivos_de_s_sin_repetir(s:list[int], t:list[int]) ->list[int]:
    lista_nueva:list[int] = []
    for i in range(len(s)):
        if not (pertenece (t, s[i])) and not (pertenece (lista_nueva, s[i])):
            lista_nueva.append(s[i])
    return lista_nueva


def elementos_exclusivos (s:list[int], t:list[int]) ->list[int]:
    res:list[int] = elementos_exclusivos_de_s_sin_repetir(s,t) + elementos_exclusivos_de_s_sin_repetir(t,s)
    return res


