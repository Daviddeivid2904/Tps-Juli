# Se dice que los perros tienen 7 an ̃os por cada an ̃o humano. Sin embargo, esto no funciona considerando 
# que los perros llegan a la adultez a los 2 an ̃os. Proponemos entonces, un mejor sistema: 
# los primeros 2 an ̃os valen 10.5 an ̃os perro, y despu ́es, cada nuevo an ̃o vale por 4 an ̃os perro. Ejemplo:
# An ̃os humanos 1 2 3 4 n
# An ̃os perro 10.5 21 25 28 21+(n−2)·4
# Hacer un programa que tome an ̃os humanos y los convierta en an ̃os perro.
# Desaf ́ıo extra: ¿Y al rev ́es? Hacer ese programa tambi ́en.

def HumanoaPerro():
    years = int(input('ingrese anios humanos: '))

    if years == 1:
        print(str(years) + ' anios humanos son equivalentes a 10.5 anios perrunos')
    elif years == 2:
        print(str(years) + ' anios humanos son equivalentes a 21 anios perrunos')
    elif years >= 3:
        yearPerro = 21 + (years-2)*4
        print(str(years) + ' anios humanos son equivalentes a ' + str(yearPerro) + ' anios perrunos')

def PerroaHumano():
    perriYears = int(input('ingrese anios perrunos: '))

    if perriYears <= 10.5:
         print(str(perriYears) + ' anios perrunos es equivalente a alrededor de 1 anio humano')
    elif perriYears <= 21:
         print(str(perriYears) + ' anios perrunos es equivalente a alrededor de 2 anios humanos')
    else:
        humanYear = -13/4 + perriYears/4

        print(str(perriYears) + ' anios perrunos son equivalentes a ' + str(humanYear) + ' anios humanos')

print('si quiere calcular la edad de un perro a un humano ingrese una P, si quiere calcular la edad de humano a perro ingrese H: ')
queQuiere = input().lower()

if queQuiere == 'p':
    PerroaHumano()
elif queQuiere == 'h':
    HumanoaPerro()
else:
    print('ingrese correctamente lo que desea')