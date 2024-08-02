
def trios(s:list[int]) -> list[list[int]]:
    res:list[list[int]] = []
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



lista = [1,2,3,4,5,6,7,8,9,10,11,12]

print(trios(lista))

print(len(trios(lista)))


