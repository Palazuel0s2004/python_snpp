def imprimir(l):
    for x in range(len(l)):
        print(f" | {l[x]}", end=" ")

def ordenar(ls, ord):# Ordenar el vector original no una copia??
    if(ord == "ASC"):
        for x in range(len(ls)-1):
            for y in range(len(ls)-1):
                if(ls[y] > ls[y+1]):
                    aux = ls[y]
                    ls[y] = ls[y+1]
                    ls[y+1] = aux
                    
def ordenar(ls, ord):# Ordenar el vector original no una copia??
    if(ord == "DESC"):
        for x in range(len(ls)-1):
            for y in range(len(ls)-1):
                if(ls[y] < ls[y+1]):
                    aux = ls[y]
                    ls[y] = ls[y+1]
                    ls[y+1] = aux

lista = [30, 20, 1, 0, 58, 200, 40, 4, 7, 15, 80, 8, 67, 2, 6]
print("Vector Original")
print(lista)
orden = "DESC"
ordenar(lista, orden)
print(end="\n")
print(f"Vector Ordenado {orden}")
print(lista)