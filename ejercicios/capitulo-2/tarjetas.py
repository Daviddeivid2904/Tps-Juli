# Primera Parte
# Hacer un programa que tome un nu ́mero (no texto) de tarjeta de cr ́edito de 16 d ́ıgitos del usuario,
# e imprima por pantalla a que red pertenece la tarjeta. Si la tarjeta no pertenece a ninguna red, 
# imprimir un mensaje de error que lo diga. Ejemplos:
# 4956618550028752 es una tarjeta Visa 5453680960593325 es una tarjeta Mastercard 7499297903955946 
# no pertenece a ninguna red
# Tip: Para obtener los d ́ıgitos de un nu ́mero podemos jugar con tomar cociente y/o resto de dividir por
# potencias de 10. Ejemplos:
# 4536 // 1000 = 4 4536% 1000 = 536 4536% 10 = 6

# Segunda Parte
# 4536 // 10 = 453
# (4536 // 10)% 100 = 53 (4536% 100)// 10 = 3
# Resulta que las American Express son de 15 d ́ıgitos, las de Visa de 14 y las de Mastercard de 16.
# Modificar el programa anterior para que no solo chequee el primer d ́ıgito sino la longitud del nu ́mero ingresado.
# Tip 1: Recuerden los and y or.
# Tip 2: Para “medir la longitud” de un nu ́mero pueden pensar en que significa tener n d ́ıgitos.
# Por ejemplo, los nu ́meros de 4 d ́ıgitos son los mayores iguales a 1000 pero menores a 10000.


tarjeta = input("ingrese el nuemro de su tarjeta: ")

def QueRed(numTarj):
    if len(numTarj) <= 16 and len(numTarj) >= 14:
        primero = numTarj[0]
        print(primero)
        if primero == '3' and len(numTarj) == 15:
            print('su tarjeta es AMERICAN EXPRESS')
            red = 'American Express'
        elif primero == '4' and len(numTarj) == 14:
            print('su tarjeta es VISA')   
            red = 'Visa'
        elif primero == '5' and len(numTarj) == 16:
            print('su tarjeta es MASTER CARD')
            red = 'Master card'
        else:
            print('su tarjeta no pertenece a ninguna red')
            red = 'Ninguna'
        return red
    else:
        print('ingreso incorrectamente la cantidad de numeros de su tarjeta')


        

print(QueRed(tarjeta))