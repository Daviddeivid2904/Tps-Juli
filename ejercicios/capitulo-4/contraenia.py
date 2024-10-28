# Pedirle al usuario que ingrese una contrasen ̃a, y e imprimir por pantalla si ingres ́o la correcta. 
# Ahora, si puso otra cosa, pedirle la contrasen ̃a nuevamente, y as ́ı sucesivamente hasta que no ingrese
# la correcta.
# Desaf ́ıo extra: Esto no es muy real. En general hay un l ́ımite a que tantos intentos podemos hacer,
# as ́ı un atacante no puede adivinar la contrasen ̃a a fuerza bruta. 
# Agregarle a nuestro programa de contrasen ̃as un l ́ımite de intentos.

constrsenia = '1234'


for i in range(4): 
    ingreso = input('ingrese la contrasenia: ')
    if ingreso == constrsenia:
        print('muy bien')
        break
    elif i+1 == 4:
        print('haz usado todos tus intentos, IMPOSTOR')
        

