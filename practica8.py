from queue import LifoQueue as Pila
from queue import Queue as Cola
import numpy as np
import random

def reverso(l:list) -> list:
    lienzo = []
    for i in range(len(l)):
        lienzo = lienzo + [l[-(i+1)]]
    return(lienzo)

def copiar_lista(s:list) -> list:
    lista_nueva:list = []
    for i in range(len(s)):
        lista_nueva.append(s[i])
    return lista_nueva
#--

def contar_lineas(archivo:str) -> int:
    arch = open(archivo,"r")
    lineas = arch.readlines()
    arch.close()
    return len(lineas)

#--

def existe_palabra_en(arch:str, palabra:str) -> str:
    estado:bool = False
    arch = open(arch,"r")
    archivo_lineas = arch.readlines()
    for linea in archivo_lineas:
        if palabra in linea:
            estado = True
    return estado

#print(existe_palabra_en("archivo.txt", "mi"))

#--

def coinciden_los_str(s1:str, s2:str) -> bool:
    estado = True
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            estado = False
    return estado



def slice(txt: str, inicio: int, final: int) -> str: #esta de pedro es la misma que mi quedarme_con_str_desde_hasta
    res: str = ""
    while inicio < final:
        res = res + txt[inicio]
        inicio += 1
    return res



def cuantas_veces_aparece_un_string(frase:str, palabra:str) -> int: #es un problema complejo el que resolvi, pero no pedian esto
    contador:int = 0
    palabra_posta = " " + palabra + " "
    palabra_posta2 = " " + palabra + "\n" #esta es por si termina con un salto de pagina o sea si una linea justo termina con moo
    longitud_palabra:int = len(palabra_posta)
    for i in range(len(frase)-longitud_palabra+1):
        if frase[i] == palabra_posta[0]:
            cont_aux:int = 0
            cont_siosi:int = 0
            while cont_siosi<longitud_palabra:
                if frase[i+cont_aux] == palabra_posta[cont_aux] or frase[i+cont_aux] == palabra_posta2[cont_aux]:
                    cont_aux = cont_aux + 1
                if cont_aux == longitud_palabra:
                    contador = contador + 1
                cont_siosi = cont_siosi + 1
    if coinciden_los_str(quedarme_con_str_desde_hasta(frase,0,len(palabra)), palabra):
        contador += 1
    if coinciden_los_str(quedarme_con_str_desde_hasta(frase,len(frase)-len(palabra),len(frase)), palabra):
        contador += 1
    return contador



def cantidad_apariciones(arch:str, palabra:str) -> str:
    contador:int = 0
    arch = open(arch,"r")
    lineas:str = arch.readlines()
    for linea in lineas:
        contador += cuantas_veces_aparece_un_string(linea,palabra)
    arch.close()
    return contador


#--
def primer_posicion_donde_hay_algo_no_espacio(s:str) -> int:
    i:int = 0
    while s[i]==" ":
        i = i + 1
    return i



def sacar_todos_los_espacios_al_principio(s:str) -> str:
    return quedarme_con_str_desde_hasta(s, primer_posicion_donde_hay_algo_no_espacio(s), len(s))


def sacar_espacios_al_principio_version_pedro(linea: str) -> str: #brillante
    res: str = ""
    p: bool = False
    i: int = 0
    
    for i in linea:
        if p and i == ' ':
            res += i
        if i != ' ':
            res += i
            p = True
                 
    return res


def es_comentario(linea:str) -> bool:
    estado = False
    if sacar_todos_los_espacios_al_principio(linea)[0] == "#":
        estado = True
    return estado

def clonar_sin_comentarios(nombre_archivo:str):
    archivo = open(nombre_archivo, 'r')
    archivo_lineas = archivo.readlines()
    archivo_nuevo_texto: str = ""

    for linea in archivo_lineas:
        if not es_comentario(linea):
            archivo_nuevo_texto += linea
            
    archivo_nuevo = open('sincomentarios.txt', 'w')
    archivo_nuevo.write(archivo_nuevo_texto)
    
    archivo_nuevo.close()
    archivo.close()


#--

def generar_numeros_al_azar_pila(n:int, desde:int, hasta:int) -> Pila:  #no se puede printear la pila entera? no
    p = Pila() # esto crea una pila vacia? si
    for i in range(n):
        num:int = random.randint(desde,hasta)
        print("un numero random es: ", num)
        p.put(num)
    return(p)

#--


def mostrarme_eltos_pila(p:Pila):
    copia_pila = Pila()
    while not(p.empty()):
        elemento = p.get()
        copia_pila.put(elemento)
        print("un elto de la pila es: ", elemento)
    while not(copia_pila.empty()):
        elem = copia_pila.get()
        p.put(elem)

def crear_pila(s:list) -> Pila:
    pila:Pila = Pila()
    for i in s:
        print("el elto que va a la pila es: ", i)
        pila.put(i)
    return pila


def copiar_pila_sin_modificarla(p:Pila) -> Pila: #copia una pila sin modificar la original
    pila_res:Pila = Pila()
    pila_auxiliar:Pila = Pila()
    while not p.empty():
        elem:int = p.get()
        pila_auxiliar.put(elem)
    while not pila_auxiliar.empty():
        elem = pila_auxiliar.get()
        pila_res.put(elem)
        p.put(elem)
    return pila_res



def cantidad_de_elementos_pila(p:Pila) -> int:
    cantidad: int = 0
    copia_pila:Pila = Pila()
    while (not (p.empty())):
        copia_pila.put(p.get())
        cantidad = cantidad + 1
    while (not (copia_pila.empty())):
           p.put(copia_pila.get())
    return cantidad


#--
def tope(p:Pila) -> int:
    elem = p.get()
    p.put(elem)
    return elem


def buscar_el_maximo(p:Pila) -> int:
    copia_pila:Pila = Pila()
    max:int = tope(p)  
    while (not p.empty()):
        elem = p.get()
        copia_pila.put(elem)
        if elem> max:
            max = elem
    while (not (copia_pila.empty())):
           p.put(copia_pila.get())
    return max

#--


def esta_bien_balanceada(s:str) -> bool: #asi hecho con lista que creo que es + facil
    estado:bool = True
    cont_abre:int = 0
    cont_cierra:int = 0
    for i in range(len(s)):
        if s[i]==")":
            cont_cierra = cont_cierra + 1
        if s[i]=="(":
            cont_abre = cont_abre + 1
        if cont_cierra > cont_abre:
            estado = False
    if cont_abre != cont_cierra:
        estado = False
    return estado

def esta_bien_balanceada_pila(s:str) -> bool:
    p_abiertos:Pila = Pila()
    estado:bool = True
    i:int = 0
    while i<len(s):
        if s[i] == "(":
            p_abiertos.put(1)
        if s[i] == ")" and p_abiertos.empty():
            estado = False
        if s[i] == ")" and not p_abiertos.empty():
            p_abiertos.get()
        i += 1
    if not p_abiertos.empty():
        estado = False
    return estado


def esta_bien_balanceada_pila_agus(s:str) -> bool:
    p_abiertos:Pila = Pila()
    estado:bool = True
    i:int = 0
    while i<len(s):
        if s[i] == "(":
            p_abiertos.put(1)
        if s[i] == ")":
            if p_abiertos.empty():
                estado = False
            else:
                p_abiertos.get()
        i += 1
    if not p_abiertos.empty():
        estado = False
    return estado

#print(esta_bien_balanceada_pila_agus("(j((h)((sa))d)a()asd((989)))"))
#--
def pertenece_string(s:list[str], x:str) -> bool:
    estado = False
    for i in range(len(s)):
        if s[i] == x:
            estado = True
    return estado

def pertenece_letra(s:str, x:chr) -> bool:
    estado = False
    for i in range(len(s)):
        if s[i] == x:
            estado = True
    return estado


def armar_numerito(s:str) -> int:
    nueva:str = ""
    numeritos:list[int] = ["0","1","2","3","4","5",'6','7','8','9']
    i:int = 0
    while pertenece_string(numeritos, s[i]):
        nueva = nueva + s[i]
        i = i+1
    transformo_a_num:int = int(nueva)
    return transformo_a_num


def evaluar_expresion(s:str) -> float:   # 3 4 + 5 * 2 -
    pila:Pila = Pila()
    operando:list[str] = ["+","-","*","/"]
    i:int = 0
    while i<(len(s)):
        if (not(pertenece_string(operando, s[i]))) and (s[i]!=" "):
            armo_num:str =""
            while (not(pertenece_string(operando, s[i])) and (s[i]!=" ")):
                armo_num = armo_num + s[i]
                i = i+1
            pila.put(armo_num)
        if pertenece_string(operando, s[i]):
            num1:float = float(pila.get())
            num2:float = float(pila.get())
            if s[i] == "+":
                res_operacion:float = num1 + num2
            if s[i] == "-":
                res_operacion:float = num2 - num1           
            if s[i] == "*":
                res_operacion:float = num1 * num2         
            if s[i] == "/":
                res_operacion:float = (num1 / num2)
            pila.put(res_operacion)
        i =i+1
    return pila

#mostrarme_eltos_pila(evaluar_expresion("3121 40 50 * + 24 -"))

#--

def mostrarme_eltos_cola(c:Cola):
    copia_cola = Cola()
    while not(c.empty()):
        elemento = c.get()                  
        copia_cola.put(elemento)
        print("el elto de la colita es: ", elemento)
    while not(copia_cola.empty()):
        elem = copia_cola.get()
        c.put(elem)


def generar_numeros_al_azar_cola(n:int, desde:int, hasta:int) -> Cola:
    cola:Cola = Cola()
    pilita = generar_numeros_al_azar_pila(n,desde,hasta)
    mostrarme_eltos_pila(pilita)
    for i in range(n):
        elto = pilita.get()
        print("el elto que va a la cola es: ", elto)
        cola.put(elto)
    return cola

#--

def cola_prueba(s:list[int]) -> Cola:
    cola:Cola = Cola()
    for i in s:
        print("el elto que va a la cola es: ", i)
        cola.put(i)
    return cola

def copiar_cola_sin_modificarla(c:Cola) -> Cola: #copia una cola sin modificar la original
    cola_res:Cola = Cola()
    cola_auxiliar:Cola = Cola()
    while not c.empty():
        elem:int = c.get()
        cola_auxiliar.put(elem)
        cola_res.put(elem)
    while not cola_auxiliar.empty():
        c.put(cola_auxiliar.get())
    return cola_res

def cantidad_de_elementos_cola(c:Cola) -> int:
    cantidad: int = 0
    copia_cola:Cola = Cola()
    while (not (c.empty())):
        copia_cola.put(c.get())
        cantidad = cantidad + 1
    while (not (copia_cola.empty())):
           c.put(copia_cola.get())
    return cantidad

#--

def armar_lista_a_partir_de_pila(p:Pila) -> list[int]:
    lista_nueva:list[int] = []
    copia_pila:Pila = Pila()
    while not p.empty():
        elto = p.get()
        print("el elto que va a la copia de la pila es: ", elto)
        copia_pila.put(elto)
    while not(copia_pila.empty()):
        elem = copia_pila.get()
        print("el elem que va a la lista es: ", elem)
        lista_nueva.append(elem)
        p.put(elem)
    return lista_nueva

def mostrar_cola_como_lista(c:Cola) -> list:
    lista_nueva:list = []
    copia_cola:Cola = Cola()
    while not c.empty():
        elto = c.get()
        copia_cola.put(elto)
    while not(copia_cola.empty()):
        elem = copia_cola.get()
        lista_nueva.append(elem)
        c.put(elem)
    return ("la cola queda: " , reverso(lista_nueva))



def armar_lista_a_partir_de_pila_otra_forma(p:Pila) -> list[int]:
    lista_nueva:list[int] = []
    copia_pila:Pila = Pila()
    while not p.empty():
        elto = p.get()
        print("el elto que va a la copia de la pila y a la lista es: ", elto)
        lista_nueva.append(elto)
        copia_pila.put(elto)
    while not(copia_pila.empty()):
        elem = copia_pila.get()
        p.put(elem)
    return lista_nueva

def armar_lista_a_partir_de_cola_otra_forma(c:Cola) -> list[int]:
    lista_nueva:list[int] = []
    copia_cola:Cola = Cola()
    while not c.empty():
        elto = c.get()
        print("el elto que va a la copia de la cola y a la lista es: ", elto)
        lista_nueva.append(elto)
        copia_cola.put(elto)
    while not(copia_cola.empty()):
        elem = copia_cola.get()
        c.put(elem)
    return lista_nueva

#--
def maximo(s:list[int]) -> int:
    max = s[0]
    for i in range(len(s)):
        if s[i]>=max:
            max = s[i]
    return max

def buscar_el_maximo_cola(c:Cola) -> int:
    lista_de_eltos:list[int] = mostrar_cola_como_lista(c)
    print("la lista es: ", lista_de_eltos)
    return maximo(lista_de_eltos)

#--
def pertenece(s:list[int],x:int) -> bool:
    estado:bool = False
    for i in range(len(s)):
        if s[i] == x:
            estado = True
    return estado

def cantidad_de_eltos_distintos(s:list[int]) -> int:
    contador = 0
    lista_nueva = []
    for i in range(len(s)):
        if not pertenece(lista_nueva,s[i]):
            contador = contador + 1
        lista_nueva.append(s[i])
    print(lista_nueva)
    return contador

def remover_primera_aparicion(s:list[int], x:int) -> list[int]: #naisu
    lista_nueva = []
    p:bool = False
    for i in range(len(s)):
        if s[i] != x:
            lista_nueva.append(s[i])
        if s[i] == x and p:
            lista_nueva.append(s[i])
        if s[i] == x:
            p = True

    return lista_nueva

def armar_secuencia_de_bingo() -> Cola[int]:
    lista_de_nums:list[int] = list(range(100))
    secuencia:Cola = Cola()
    while len(lista_de_nums)>0:
        bolita:int = random.choice(lista_de_nums)
        print("salio el num: ", bolita)
        secuencia.put(bolita)
        lista_de_nums.remove(bolita)
    return secuencia

def generar_carton() -> list[int]:
    lista_nums = []
    nums_posibles:list[int] = range(100)
    for i in range(12):
        num:int = random.choice(nums_posibles)
        lista_nums.append(num)
        nums_posibles = remover_primera_aparicion(nums_posibles, num)
    return lista_nums


def jugar_carton_de_bingo(carton:list[int], bolillero: Cola[int]) -> int: #esta es la forma mas normal, pero hay otra, sin usar cola
    contador:int = 0       #cuento de como quedo la cola, cuando esta el primer valor que este en el carton, la rta es 100 - eso
    carton_copia:list[int] = copiar_lista(carton)
    copia_bolillero:Cola = copiar_cola_sin_modificarla(bolillero)
    while len(carton_copia)>0:
        elem:int = copia_bolillero.get()
        if pertenece(carton_copia, elem):
            carton_copia = remover_primera_aparicion(carton_copia, elem)
        contador += 1
    return contador

'''
bingo:Cola = armar_secuencia_de_bingo()
mostrarme_eltos_cola(bingo)
print("el bolillero es" , mostrar_cola_como_lista(bingo))

carton = generar_carton()

print("el carton es" ,carton)

print("fueron tantas jugadas :", jugar_carton_de_bingo(carton, bingo))
'''

#--

def crear_queue_hospital(pacientes:list[(str,str)]) -> Cola[(int,str,str)]:
    cola_pacientes:Cola[(int,str,str)] = Cola()
    for i in range(len(pacientes)):
        elem = (random.randint(1,10),pacientes[i][0],pacientes[i][1])
        cola_pacientes.put(elem)
    return cola_pacientes


def n_pacientes_urgentes(c:Cola[(int,str,str)]) -> int:
    copia_cola:Cola = copiar_cola_sin_modificarla(c)
    contador:int = 0
    while not copia_cola.empty():
        elem = copia_cola.get()
        if elem[0] <= 3:
            contador += 1
    return contador


#colita = crear_queue_hospital([("pigi","general"),("eitor","traumatologia"),("gon","hema"),("kilua","nano")])

#--
# 

def crear_cola_banco() -> Cola[(str,int,bool,bool)]:
    cola:Cola = Cola()
    nombre_y_apellido:str = str(input("ingrese nombre y apellido: "))
    while nombre_y_apellido != "fin":
        dni:int = int(input("ingrese DNI: "))
        tipo_cuenta:bool = bool(input("ingrese True si es preferencial o False sino: "))
        prioridad:bool = bool(input("indique True si tiene prioridad sino False: "))
        elem = (nombre_y_apellido, dni, tipo_cuenta, prioridad)
        cola.put(elem)
        nombre_y_apellido:str = input("ingrese nombre y apellido: ")
    return cola


def atencion_a_clientes(c:Cola[(str,int,bool,bool)]) -> Cola[(str,int,bool,bool)]:
    copia_cola:Cola = copiar_cola_sin_modificarla(c)
    cola_general:Cola = Cola()
    cola_prioridad:Cola = Cola()
    cola_preferencial_y_no_prioridad:Cola = Cola()
    cola_resto:Cola = Cola()

    while not copia_cola.empty():
        elem = copia_cola.get()
        if elem[3] == True:
            cola_prioridad.put(elem)
        elif elem[2] == True:
            cola_preferencial_y_no_prioridad.put(elem)
        else:
            cola_resto.put(elem)
    
    while not cola_prioridad.empty():
        cola_general.put(cola_prioridad.get())
    while not cola_preferencial_y_no_prioridad.empty():
        cola_general.put(cola_preferencial_y_no_prioridad.get()) 
    while not cola_resto.empty():
        cola_general.put(cola_resto.get())
    
    return cola_general

'''
cola_banco = atencion_a_clientes(crear_cola_banco())
        
print("la cola es: ")
mostrarme_eltos_cola(cola_banco)

print("segun la pc: ", cola_banco.queue)
'''

#--
'''
def imprimir_eltos_diccionario(d:dict):
    items = d.items()
    for i in range(len(items)):
        print(d[i])

def imprimir_eltos_dicc(d:dict):
    for c,v in d.items():
        print(v)

def imprimir_eltos_dicc(d:dict):
    for i in d.items():
        print(i)


diccionario:dict = {}
diccionario[0] = "ger"
diccionario[2] = "pigi"
diccionario[1] = "eitor"


print(diccionario.values())
print(diccionario.keys())
print(diccionario.items())
'''
#--
def quedarme_con_str_desde_hasta(s:str, desde:int, hasta:int) -> str:  
    frase_nueva = ""
    for i in range(desde,hasta):
        frase_nueva = frase_nueva + s[i]
    return frase_nueva

def obtener_palabra(s:str) -> str:
    palabra:str = ""
    j:int  = 0
    if pertenece(s," "):
        while s[j] != " " and j<len(s):
            palabra = palabra + s[j]
            j +=1
    else:
        return s
    return palabra

def separar_palabra_clase(linea:str) -> list[str]: #version clase asuminedo que no hay espacios al princ y al final
    res:list[str] = [] #hay que arreglarla esta
    palabra:str = ""
    for letra in linea:
        if letra != " ":
            palabra = palabra + letra
        else:
            res.append(palabra)
            palabra = ""
    return res

def obtener_lista_palabras(s:str) -> list[str]:
    lista_palabras:list[str] = []
    texto:str = s
    while (len(texto)>0 ):
        palabra:str = obtener_palabra(texto)
        texto = quedarme_con_str_desde_hasta(texto, len(palabra)+1, len(texto))
        lista_palabras = lista_palabras + [palabra]
    return lista_palabras


def obtener_lista_de_palabras_todas(archivo_nombre:str) -> list[list[str]]:
    archivo = open(archivo_nombre)
    lineas = archivo.readlines()
    lista_de_listas = []
    for i in range(len(lineas)):
        lista = obtener_lista_palabras(lineas[i])
        lista_de_listas = lista_de_listas + lista
    archivo.close()
    return lista_de_listas


def borrar_salto_de_linea(s:str) -> str:
    if pertenece_letra(s,"\n"):
        return (quedarme_con_str_desde_hasta(s,0,len(s)-1))
    else:
        return s

def borrar_salto_linea_a_toda_la_lista(s:list[str]) -> list[str]:
    lista_nueva = []
    for i in s:
        lista_nueva = lista_nueva + [borrar_salto_de_linea(i)]
    return lista_nueva


def cantidad_de_palabras(s:list[str], x:int) -> int:
    contador:int = 0
    for i in range(len(s)):
        if len(s[i]) == x:
            contador += 1
    return contador

def longitud_maxima(s:list[str]) -> int:
    max = 0
    for i in range(len(s)):
        if len(s[i])> max:
            max = len(s[i])
    return max


def armar_lista_palabras_bien(nombre_archivo:str) -> list[str]:
    lista: list[str] = borrar_salto_linea_a_toda_la_lista(obtener_lista_de_palabras_todas(nombre_archivo))
    return lista


def agrupar_por_longitud(nombre_archivo:str) -> dict:   #esto hacerlo de nuevo fijandome si ya existe la clave
    lista_palabritas = armar_lista_palabras_bien(nombre_archivo)
    long_max:int = longitud_maxima(lista_palabritas)
    d:dict = dict()
    for i in range(1,long_max+1):
        if cantidad_de_palabras(lista_palabritas,i)!=0:
            d[i] = cantidad_de_palabras(lista_palabritas, i)
    return d


def agrupar_por_longitud_otra_forma(nombre_archivo:str) -> dict:
    lista_palabritas:list[str] = armar_lista_palabras_bien(nombre_archivo)
    d:dict = dict()
    for i in range(len(lista_palabritas)):
        longitud_palabra:int = len(lista_palabritas[i])
        if longitud_palabra in d.keys():
            d[longitud_palabra] = d[longitud_palabra] + 1
        else:
            d[longitud_palabra] = 1
    return d


'''
lista_palabras_con_salto:list[str]= obtener_lista_de_palabras_todas("archivo.txt")

lista_palabras = borrar_salto_linea_a_toda_la_lista(lista_palabras_con_salto)
print(lista_palabras)


diccionario_longitud:dict = agrupar_por_longitud("archivo.txt")

print(diccionario_longitud)

diccionario_longitud_otra_forma:dict = agrupar_por_longitud_otra_forma("archivo.txt")

print(diccionario_longitud_otra_forma)
'''
#--

def cuantas_veces_aparece_un_elto_en_una_lista(s:list, x) -> int:
    contador:int = 0
    for i in range(len(s)):
        if s[i] == x:
            contador += 1
    return contador

def crear_diccionario_frecuencia_palabras(nombre_archivo:str) -> dict:
    lista_palabras:list[str] = armar_lista_palabras_bien(nombre_archivo)
    d:dict = dict()
    for i in range(len(lista_palabras)):
        d[lista_palabras[i]] = cuantas_veces_aparece_un_elto_en_una_lista(lista_palabras,lista_palabras[i])
    return d


#dicc = crear_diccionario_frecuencia_palabras("archivo.txt")




def palabra_mas_frecuente(nombre_archivo:str) -> str:   #naisuuuu
    d:dict = crear_diccionario_frecuencia_palabras(nombre_archivo)
    max:int = 0
    clave_max = "no hay palabras en este archivo"
    for c,v in d.items():
        if v>max:
            max = v
            clave_max = c
    return clave_max


def palabra_mas_frecuente_otra_forma(nombre_archivo:str) -> str:
    d:dict = crear_diccionario_frecuencia_palabras(nombre_archivo)
    max:int = 0
    clave_max :str
    for clave in d.keys():
        if d[clave] > max:
            max = d[clave]
            clave_max = clave
    return clave_max

#print(palabra_mas_frecuente_otra_forma("archivo.txt"))

#--
'''
def pertenece_elto_a_lista_str(s:list[str],x:str) -> bool:
    estado:bool = False
    for i in range(len(s)):
        if s[i] == x:
            estado = True
    return estado

def crear_lista_de_claves(dict:dict) -> list: #sino se puede lo de abajo, uso esto
    lista_nueva = []
    for c in dict.keys():
        lista_nueva.append(c)
    return lista_nueva


def visitar_sitio(historiales:dict[str, Pila[str]], usuario:str, sitio:str):
    if not usuario in historiales.keys():    #DUDA, se puede este if elemento in conjunto aca???
        historiales[usuario] = crear_pila([sitio])
    else:
        historiales[usuario].put(sitio)


pila_usuario1:Pila[str] = crear_pila(["google.com","facebook.com", "youtube.com"])
pila_usuario2:Pila[str] = crear_pila(["siu guarani","campus","mtga","spotify"])
pila_usuario3:Pila[str] = crear_pila(["sims","destiny","overwatch"])

diccionario_historiales:dict = dict()
diccionario_historiales["usuario_pigi"] = pila_usuario1
diccionario_historiales["usuario_gon"] = pila_usuario2
diccionario_historiales["usuario_kilua"] = pila_usuario3

visitar_sitio(diccionario_historiales, "usuario_pigi", "poker.com")
visitar_sitio(diccionario_historiales, "usuario_gon", "ciberjuegos.com")
visitar_sitio(diccionario_historiales, "usuario_HISOKA", "crunchyroll.com")

mostrarme_eltos_pila(diccionario_historiales["usuario_HISOKA"])


def navegar_atras(historiales:dict[str, Pila[str]], usuario:str):
    sitio_actual = historiales[usuario].get()
    sitio_anterior = historiales[usuario].get()
    historiales[usuario].put(sitio_actual)
    historiales[usuario].put(sitio_anterior)

print("la de pigi quedo:")
mostrarme_eltos_pila(diccionario_historiales["usuario_pigi"])

navegar_atras(diccionario_historiales, "usuario_pigi")

print("si navega hacia atras, queda: ")
mostrarme_eltos_pila(diccionario_historiales["usuario_pigi"])
'''
#--
'''

def agregar_producto(inventario:dict, nombre:str, precio:float, cantidad:str):
    inventario[nombre] = {"precio":precio, "cantidad":cantidad}


def actualizar_stock(inventario:dict, nombre:str, cantidad:int):
    for clave in inventario[nombre].keys():
        if clave == "cantidad":
            inventario[nombre][clave] = cantidad

def actualizar_stock_otra_forma(inventario:dict, nombre:str, cantidad:int):
    inventario[nombre]['cantidad'] = cantidad


def actualizar_precio(inventario:dict, nombre:str, precio:float):
    for clave in inventario[nombre].keys():
        if clave == "precio":
            inventario[nombre][clave] = precio


def calculcar_valor_inventario(inventario:dict) -> float:  #naisuu
    valor_total:float = 0
    for producto in inventario.keys():
        cantidad_producto:int = 0
        precio_producto:float = 0
        valor_producto:float = 0
        for sub_clave in inventario[producto].keys():
            if sub_clave == "precio":
                precio_producto = inventario[producto][sub_clave]
            if sub_clave == "cantidad":
                cantidad_producto = inventario[producto][sub_clave]
        valor_producto = precio_producto * cantidad_producto
        valor_total = valor_total + valor_producto
    return valor_total


inventario:dict[str, dict[str, float]] = dict()

agregar_producto(inventario, "remera", 12.5, 2)
agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantalon", 30.0, 30)
agregar_producto(inventario, "zapatillas", 150.0, 60)


print(inventario)
print("el dicc de remera es: ", inventario["remera"])
print("las claves de remera son", inventario["remera"].keys())


actualizar_stock_otra_forma(inventario, "Camisa", 3000)
actualizar_precio(inventario, "Pantalon", 180.99)
print(inventario)
            
print("el valor total es: ", calculcar_valor_inventario(inventario))
'''

dicc1 = dict()
dicc1[1] = "uno"
dicc1[2] = "dos"
dicc1[3] = "tres"

dicc2 = {4:"four",5:"five",6:"six"}


print(list((dicc1.items()))[1])

print(dicc2.items())

print("uno" in dicc1)