
# def empleado(nombre,ventas,importe):
#     comision = importe*0.05
#     total = 900000 + comision
#     print(nombre,'vendio',ventas,'muebles con un valor total de',importe,'por lo que su comision es de $',comision,'con un total de $',total)
# empleado("juan",50,5000)        
        
notas = [] 
for i in range(5):
    nota = int(input('Ingrese la nota: '))
    while nota < 0 or nota >10:
        print('ingrse una nota valida')
        nota = int(input('Ingrese la nota: '))
    notas.append(nota) 
print('El promedio de las notas es de ' + str(sum(notas)/5))
    
