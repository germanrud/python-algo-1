def pruebitaDuplicar(lista:list, numerito:int):
    lista *= 2
    numerito *= 2

    print(lista, numerito)


l:list = [1,2,3]
n:int = 2

num = 10

pruebitaDuplicar(l,n)


print(l)  #no deberia pasarse por referencia y quedar [1,2,3,1,2,3] como en la teorica???
print(n)

