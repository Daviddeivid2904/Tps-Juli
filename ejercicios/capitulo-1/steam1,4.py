# Steam es un plataforma para comprar juegos de computadora. Comprar juegos en Steam es barato, pero no tan barato como parece. Al precio que aparece, se le debe agregar:
# impuesto a las ganancias (35 %) impuesto PAIS (8 %)
# IVA (21 %)
# Hacer un programa en python que le pueda ingresar el precio de un juego 
# en Steam, y me devuelva por pantalla, detallado, cuanto pago por cada impuesto
# y cuanto termino pagando en total. No solo se debe decir los valores, se debe 
# imprimir a que corresponden en la misma l ́ınea. 
# TIP: la funci ́on str() convierte cosas a texto.

precio = int(input("Ingrese el precio del juego: "))

iva = precio * 0.21
impGan = precio * 0.35
impPais = precio * 0.08
print("iva: " + str(iva)+'$')
print("impuesto pais: " + str(impPais)+'$')
print("impuesto ganancia: " + str(impGan)+'$')
print("Costo total: " + str(precio+iva+impGan+impPais)+'$')
