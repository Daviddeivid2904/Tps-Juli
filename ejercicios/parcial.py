cantidad = 0
queso1=0
queso2=0
pedidos = -2
while pedidos != -1:
    pedidos = int(input('ingrese la cantidad de pedidos entre 1 y 300: '))
    if pedidos != -1:
        while (pedidos < 1 or pedidos >300):
            pedidos=int(input('ingreso incorrecto, ingrese la cantidad de pedidos nuevamente entre 1 y 300: '))  
        cantidad = cantidad+pedidos
        tipo = int(input('ingrese el tipo de queso,1 si es normal 2 si es saborizadi: '))
        while tipo < 1 or tipo > 2:
            tipo=int(input('ingreso incorrecto, ingrese el tipo de queso nuevamente 1 si es normal 2 si es saborizado: '))
        if(tipo == 1):
            queso1 = queso1+pedidos
        elif(tipo == 2):
            queso2 = queso2+pedidos
porcentaje1 = (queso1 * 100)/cantidad
porcentaje2 = (queso2 * 100)/cantidad
print('la cantidad total de quesos pedidos fue de',cantidad)
print('la cantidad total del queso 1 fue de',queso1)
print('la cantidad total del queso 2 fue de',queso2)
print('el porcentaje del queso 1 fue de',round(porcentaje1,2))
print('el porcentaje del queso 2 fue de',round(porcentaje2,2))
if(queso1 > queso2):
    print('el queso 1 tuvo mas pedidos que el 2')
elif(queso2 == queso1):
    print('el queso 2 y el queso 1 tivieron la misma cantidad de pedidos')
else:
     print('el queso 2 tuvo mas pedidos que el 1')
