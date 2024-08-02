import math


def imprimir_hola_mundo():
    print("Hola Mundo!")
    return None


def imprimir_un_verso():
    print("hola a todos yo soy el leon\nrujo la bestia en medio de la avenida\ntodos corrieron sin entender")


def raizDe2():
    print(round(math.sqrt(2), ndigits= 4))


def factorial_de_dos() -> int:
    print(2)

def perimetro() -> float:
    print(2*math.pi)

#---------------

def imprimir_saludo (nombre: str):
    print("Hola " + nombre)


def raiz_cuadrada_de(numero: int) -> float:
    print(math.sqrt(numero))

def farenheit_a_celsius(temp_far : float) -> float:
    print((temp_far - 32) *(5/9))

def imprimir_dos_veces(estribillo: str):
    print(estribillo * 2)

def es_multiplo_de (n:int , m:int) -> bool:
    if n%m == 0:
        return True
    else:
        return False

def valor_absoluto(n:int) -> int:
    if n>=0:
        return(n)
    else:
        return(-n)

def esMultiploDeWhile (n:int, m:int) -> bool:
    x = valor_absoluto(n)
    y = valor_absoluto(m)
    while x >= y:
        x = x - y
        print(x)
    if x == 0:
        return True
    else:
        return False


def es_par(numero: int) -> bool:
    return (es_multiplo_de(numero,2))

def techo(num:float) -> int:
    if num//1 == num:
        return(num)
    else:
        return(num//1 +1)


def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    return (techo ((comensales * min_cant_de_porciones) / 8) )

#--

def alguno_es_0 (num1: int, num2: int) -> bool:
    return(num1==0 or num2==0)

def ambos_son_0 (num1: int, num2: int) -> bool:
    return(num1==0 and num2==0)

def es_nombre_largo (nombre: str) -> bool:
    return (len (nombre) >= 3 and len (nombre) <= 8)

def es_bisiesto (anio: int) -> bool:
    return((anio % 400 == 0) or (anio % 4==0 and anio % 100 != 0 ))

#--

def peso_pino (altura : float) -> float:
    if altura <= 3:
        return (altura * 100 * 3)
    else:
        return (900 + ((altura-3) * 100 * 2))

def peso_pino_while (alt : int) -> int:
    x = alt
    peso = 0
    while x!=0:
        if x>3:
            peso = peso + 200
            x = x-1
        else:
            peso = peso + 300
            x = x-1
        
    return (peso)


def es_peso_util (peso : int) -> bool:
    return(peso>=400 and peso<=1000)


def sirve_pino (altura : int) -> bool:
    return(es_peso_util(peso_pino_while(altura)))

#--

def devolver_el_doble_si_es_par(numero : int) -> int:
    x = numero
    if es_par(x):
        return (2*x)
    else:
        return x

def devolver_valor_si_es_par_sino_el_que_sigue(numero: int) -> int:
    x = numero
    if es_par(x):
        return x
    else:
        return x+1

def devolver_valor_si_es_par_sino_el_que_sigueifif (numero: int) -> int:  #ambas funcionan creo
    x=numero
    if es_par(x):
        return x
    if not (es_par(x)):
        return x+1


def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(n:int) ->int: #interpreto como que si es de 9 y de 3 gana el de 9
    if es_multiplo_de(n,9):
        return 3*n
    elif es_multiplo_de(n,3):
        return 2*n
    else:
        return n

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9ifif(n:int) ->int:
    if es_multiplo_de(n,9):
        return 3*n
    if es_multiplo_de(n,3):
        return 2*n
    else:
        return n


def lindo_nombre(nombre: str):
    if len(nombre) >= 5:
        print("Tu nombre tiene muchas letras!")
    else:
        print("Tu nombre tiene menos de 5 letras")

def elRango(num:int) -> str:
    if num<5:
        print("Menor a 5")
    if num>=10 and num<=20:
         print("Entre 10 y 20")
    if num>20:
        print("Mayor a 20")
    
def vacaciones_o_laburo (sexo:str , edad:int) -> str:
        if edad>=65:
            return("vacaciones")
        if edad<65 and edad>= 18:
         if sexo=="M" and edad>= 60:
            return("vacacionees")
         else:
                return("te toca trabajar")
        if edad < 18:
            return("vacaciones")


def vacac_o_lab(sexo:str , edad:int) -> str:
    if edad<18:
        return("vacaciones")
    if edad<60:
        return("te toca trabajar")
    if edad<65 and sexo=="M":
        return("vacaciones")
    if edad<65 and sexo=="H":
        return("te toca trabajar")
    return ("vacaciones")


#--

def del1al10(): 
    x = 1
    while x <=10:
        print(x)
        x=x+1


def paresDel10Al40(): 
    x=10
    while x<=40:
        if es_par(x):
            print(x)
            x = x+1
        else:
            x=x+1

def paresDel10Al40OPCB():
    x=10
    while x<=40:
        print(x)
        x+=2

def eco():
    x=10
    while x!=0:
        print("eco")
        x = x-1

def viaje_en_el_tiempo(partida:int ,llegada:int ):
    x = partida
    while x!=llegada:
        x = x-1
        print("Viajo un ano al pasado, estamos en el ano:  " , x)

def viajeTiempo20(partida:int):    #interpreto lo mas cercano pero anterior 
    x = partida
    while x>384:
        x = x-20
        print("viajo 20 en el tiempo, el ano es: " , x)

def viajeTiempo20mascercano(partida:int):   #interpreto ms cercano de cualquier forma
    x = partida
    while (x>384 and (not(x-384 < 384 - (x-20)))):
        x-=20
        print("viajo 20 , el ano es: " , x)



def cuentaRegresiva(n:int):
    x = n
    while x>=1:
        print(x)
        x = x-1
    print("Despegue")

def cuentaRegresivaOPCB(n:int):
    x = n
    while x>1:
        print(x)
        x = x-1
    print(x)
    print("Despegue")


#--

def del1al10RANGE():
    for i in range (1,11,1):
        print(i)


def paresDel1al40RANGE():
    for i in range (10,41,2):
        print (i)

def ecoRANGE():
    for i in range (1,11,1):
        print("eco")


def cuentaRegresivaRANGE(n:int):
    for i in range (n,0,(-1)):
        print(i)
    print("Despegue")

def viaje_en_el_tiempoRANGE(partida:int, llegada:int):
    x=partida
    for i in range(x-1, llegada-1, -1):
        print("viaje un ano, el ano es: ", i)


def viaje20RANGE(partida:int): #el mas cercano pero anterior o igual
    x=partida
    for i in range(partida-20, 384-20,-20):
        print("viaje 20, el ano es: " , i)
    
#--

def rt(x:int, g:int) -> int:
    g = g+1
    return x + g

g: int = 0
def ro(x:int)-> int:
    global g
    g = g+1
    return x+g


def rt(x:int, g:int) -> int:
    #estado a
    g = g+1 # estado b, vale g = g@a + 1
    return x + g # vale x@a + g@b

g : int = 0 # estado a 
def ro(x:int) -> int: 
    # estado b 
    global g
    g = g + 1 # estado c,  vale g == g@a + 1
    return x + g # vale x@b + g@c