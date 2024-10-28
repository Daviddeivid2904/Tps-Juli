notas = [] 
for i in range(5):
    nota = int(input('Ingrese la nota: '))
    while nota < 0 or nota >10:
        print('ingrse una nota valida')
        nota = int(input('Ingrese la nota: '))
    notas.append(nota) 
print('El promedio de las notas es de ' + str(sum(notas)/5))
    
