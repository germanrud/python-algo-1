
def mejores_precios(super1:list[(str,float)] , super2:list[(str,float)]) -> list[(str,float)]:
    res:list[(str,float)] = []
    for i in range(len(super1)):
        if super1[i][1]<=super2[i][1]:
            res.append(super1[i])
        else:
            res.append(super2[i])
    return res


#--
'''
def obtener_lista_se_seguidillas(calificaciones:list[int], nota_minima:int) -> list[list[int]]:
    lista_de_listas:list[list[int]] = []
    i:int = 0
    while i<len(calificaciones):
        lista_de_nums:list[int] = []
        j:int = i
        if calificaciones[i]>=nota_minima:
                while j<len(calificaciones) and calificaciones[j]>=nota_minima:
                    lista_de_nums.append(calificaciones[j])
                    j+=1
                lista_de_listas.append(lista_de_nums)
                lista_de_nums = []
                i = j
        else:
             i+=1
    return lista_de_listas
'''


def obtener_lista_se_seguidillas(calificaciones:list[int], nota_minima:int) -> list[list[int]]: #consular este
    lista_de_listas:list[list[int]] = []
    i:int = 0
    while i<len(calificaciones):
        lista_de_nums:list[int] = []
        while i<len(calificaciones) and calificaciones[i]>=nota_minima:
            lista_de_nums.append(calificaciones[i])
            i+=1
        if lista_de_nums!= []:
            lista_de_listas.append(lista_de_nums)
        lista_de_nums = []
        i+=1
    return lista_de_listas



def obtener_lista_de_seguidillas_version_mateo(calificaciones:list[int], nota_minima:int) -> list[list[int]]:
    lista_de_listas:list[list[int]] = []
    lista_de_nums:list[int] = []
    for i in range(len(calificaciones)):
        if calificaciones[i]>=nota_minima:
            lista_de_nums.append(calificaciones[i])
            if i==len(calificaciones)-1:
                lista_de_listas.append(lista_de_nums)
        if  calificaciones[i]<nota_minima and lista_de_nums!= []:
            lista_de_listas.append(lista_de_nums)
            lista_de_nums = []
    return lista_de_listas



def subsecuecias(calificaciones: list[int], nota_minima: int) -> list[list[int]]:
  lista_subsecuecias = []
  subsecuencia = []
  for nota in calificaciones:
    if nota >= nota_minima:
      subsecuencia.append(nota)
    elif subsecuencia != []:
      lista_subsecuecias.append(subsecuencia)
      subsecuencia = []

  lista_subsecuecias.append(subsecuencia)
   
    
  return lista_subsecuecias


def long_maxima(s:list[list[int]]) -> int:
    maximo:int = 0
    for i in range(len(s)):
        if len(s[i])>=maximo:
            maximo = len(s[i])
    return maximo

def seguidilla(s:list[int], nota_minima:int) -> int:
    return long_maxima(obtener_lista_de_seguidillas_version_mateo(s,nota_minima))

lista = [90,1,99,78]

print(subsecuecias(lista, 60))


'''
def obtener_lista_se_seguidillas2(calificaciones:list[int], nota_minima:int) -> list[list[int]]: #usando break que no va
    lista_de_listas:list[list[int]] = []
    i:int = 0
    while i<len(calificaciones):
        lista_de_nums:list[int] = []
        while calificaciones[i]>=nota_minima:
            lista_de_nums.append(calificaciones[i])
            i+=1
            if i==len(calificaciones):
                break
        if lista_de_nums!= []:
            lista_de_listas.append(lista_de_nums)
        lista_de_nums = []
        i+=1
    return lista_de_listas
'''

#--


def hay_elem_en_pos_par(s:list[int], elem:int) -> bool:
    estado = False
    for i in range(len(s)):
        if i%2==0 and s[i]==elem:
            estado = True
    return estado


def elem_en_pos_pares(s:list[list[int]], elem:int) -> list[bool]:
    res: list[bool] = []
    for i in range(len(s)):
        if hay_elem_en_pos_par(s[i], elem):
            res.append(True)
        else:
            res.append(False)
    return res

'''
M= [
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[9, 8, 7, 6, 4, 5, 3, 2, 1],
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 4, 0, 0, 0],
[0, 1, 0, 0, 6, 0, 0, 1, 0],
]


print(elem_en_pos_pares(M, 1))
'''

#--

def pertenece(s:list, x) -> bool:
    estado = False
    for i in range(len(s)):
        if s[i] == x:
            estado = True
    return estado


def viajes_por_dia(viajes_diarios:dict[int,list[str]], usuarios:list[str]) -> dict[str,int]:
    res:dict = dict()
    for i in range(len(usuarios)):
        contador:int = 0
        for clave in viajes_diarios.keys():
            if pertenece(viajes_diarios[clave],usuarios[i]):
                contador = contador + 1
        res[usuarios[i]] = contador
    return res


'''
viajes_diarios:dict = {1 : ["Juan", "Maria"], 2 : ["Marcela","Juan"], 3:["eitor"]}
usuarios = ["Juan", "Maria", "Marcela","piglet"]

dicc_viajes_por_dia = viajes_por_dia(viajes_diarios, usuarios)

print(dicc_viajes_por_dia)
'''
