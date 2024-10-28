import random

facturaciones = []
for i in range(10):
    facturado = random.randint(1000,50000)
    facturaciones.append(facturado)

def suma(lista):
    total = 0
    for k in range(len(lista)):
        total = total + lista[k]
    return total

def promedio(lista):
    return suma(lista)/len(lista) 

def maximo(lista):
    maxi = 0
    for j in range(len(lista)):
        if lista[j] > maxi:
            maxi = lista[j]
    return maxi

def minimo(lista):
    mini = 100000
    for j in range(len(lista)):
        if lista[j] < mini:
            mini = lista[j]
    return mini
def esta (lista):
    numero = int(input("ingrese una cantidad para ver si se encuentra entre las facturaciones: "))
    for j in range(len(lista)):
        if lista[j] == numero:
            return "su cantidad se encuentra entre las facturaciones "
    return "su cantidad no se encuentra entre las facturaciones" 


aux = 0
for k in range(len(facturaciones)):
    for j in range(len(facturaciones)-1):
        if facturaciones[j] > facturaciones[j+1]:
            aux = facturaciones[j]
            facturaciones[j] = facturaciones[j+1]
            facturaciones[j+1] = aux
def porcentaje(lista):
    return (suma(lista)*100)/1000000
print("Una empresa tuvo estas facturaciones en un dia:",facturaciones)
print("el total facturado fue de:",suma(facturaciones))
print("el promedio de facturacion por venta fue de:", promedio(facturaciones))
print("la compra de mas valor fue de $",maximo(facturaciones),"y la de menos valor fue de $",minimo(facturaciones))
print(esta(facturaciones))
print('la empresa genera un promedio de $1.000.000 a la semana, por lo que este dia genero un',round(porcentaje(facturaciones),2),"%" " de la semana")

    