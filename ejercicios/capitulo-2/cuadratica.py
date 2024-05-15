# Hacer un programa que pida a, b y c, y calcule las ra ́ıces de la cuadra ́tica.

a = int(input('ingrese A: '))
b = int(input('ingrese B: '))
c = int(input('ingrese C: '))

def Cuadratica(a,b,c):

    discriminante = b*b+(-4*a*c)
    if discriminante<0:
        print('no tiene raices reales')
    else:
        raices = []
        equis1 = (-b+(discriminante**0.5))/(2*a)
        equis2 = (-b-(discriminante**0.5))/(2*a)
        raices.append(equis1)
        raices.append(equis2)
        print(str(raices[0]) + ' y ' + str(raices[1]))
        return raices

raicesfinales = Cuadratica(a,b,c)

