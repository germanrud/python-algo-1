
def es_fila_valida(s:list[int]) -> bool:
        estado:bool = True
        acum:list[int] = []
        for i in range(len(s)):
                elem:int = s[i]
                if elem in acum and elem != 0:
                        estado = False
                acum.append(elem)
        return estado


def trasponer(m:list[list[int]]) -> list[list[int]]:
        res:list[list[int]] = []
        for i in range(len(m[0])):
                col_i:list[int] = []
                for j in range(len(m)):
                        col_i.append(m[j][i])
                res.append(col_i)
        return res


def esMatrizValida(m:list[list[int]]) -> bool:
        estado:bool = True
        for i in range(len(m)):
                if not(es_fila_valida(m[i])):
                        estado = False
        return estado


def esSudokuValido(m:list[list[int]]) -> bool:
        estado:bool = False
        if esMatrizValida(m) and esMatrizValida(trasponer(m)):
                estado = True
        return estado




