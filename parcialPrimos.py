
def es_primo(n:int) -> bool:
    res:bool = True
    if n==1:
        res = False
    if n== 0:
        res = False
    for i in range(2,n):
        if n%i==0:
            res = False
    return res


def ult3(n:int) -> int:
    num:str = str(n)
    res:str = ""
    longitud:int = len(num)
    for i in range(longitud-3,longitud):
        res = res + num[i]
    return int(res)


def filtrar_codigos_primos(codigos_barra:list[int]) -> list[int]:
    res:list[int] = []
    for numero in codigos_barra:
        if es_primo(ult3(numero)):
            res.append(numero)
    return res

'''
lista = [123123,3134,3455,122,411,123002,1213011,313101]

print(filtrar_codigos_primos(lista))
'''


